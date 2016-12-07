from django import forms
from .models import WarnedUser


class WarnedUserForm(forms.ModelForm):

    class Meta:
        model = WarnedUser
        fields = ['user_id']
        widgets = {
            'user_id': forms.TextInput(
                attrs={'id': 'warning-box',
                       'placeholder': 'Facebook username or profile ID'}
            ),
        }
        labels = {'user_id': ''}
