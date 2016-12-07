from django.shortcuts import render
from .forms import WarnedUserForm
from .models import WarnedUser

import re

def home(request):
    '''
    If Facebook username or profile ID is POSTed to this view,
    it increments the warning_count of the associated user_id by 1
    or create WarnedUser object if it doesn't exist.
    '''
    warned_user = None
    pattern = re.compile(r"(http|https):\/\/?(?:web.)?facebook.com\/.+\?+(fref)+=(nf|ufi)")
    if request.method == 'POST':
        form = WarnedUserForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            try:
                match = pattern.search(user_id)
                if match:
                    # TODO: Add a mechanism to seek out the username from the link.
                    link = match.group()
                    clean_link = link[25:]
                    link_chars = []
                    for i in clean_link:
                        if i != '?':
                            link_chars.append(i)
                        else:
                            break
                    username = ''.join(link_chars)
                else:
                    username = user_id

                warned_user = WarnedUser.objects.get(user_id=username)
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
