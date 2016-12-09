from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import WarnedUserForm
from .models import WarnedUser


@login_required
def home(request):
    '''
    If Facebook username or profile ID is POSTed to this view,
    it increments the warning_count of the associated user_id by 1
    or create WarnedUser object if it doesn't exist.
    '''
    warned_user = None
    if request.method == 'POST':
        form = WarnedUserForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            try:
                warned_user = WarnedUser.objects.get(user_id=user_id)
                warned_user.warning_count += 1
                warned_user.save()
            except WarnedUser.DoesNotExist:
                warned_user = form.save()
    else:
        form = WarnedUserForm()

    context = {
        'form': form,
        'warned_user': warned_user
    }
    return render(request, 'home.html', context)
