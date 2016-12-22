from django import forms

from .facebook import get_fb_username_or_id


class FacebookProfileUrlForm(forms.Form):
    '''
    This form will be used to get the facebook profile url of the warned user.
    '''
    attributes = {
        'id': 'warning-box',
        'placeholder': 'https://www.facebook.com/murad.takla?fref=nf'
    }
    user_id = forms.CharField(widget=forms.TextInput(attrs=attributes),
                              label='')

    def clean_user_id(self):
        '''Extract the facebook username or profile id from url'''
        fb_profile_link = self.cleaned_data['user_id']
        user_id = get_fb_username_or_id(fb_profile_link)
        if not user_id:
            raise forms.ValidationError('Invalid facebook profile URL pattern',
                                        code='invalid')
        return user_id
