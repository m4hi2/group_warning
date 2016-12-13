'''
The whole purpose in life of this file is to handle various stuff related to facebook and this project.
'''

import re

def get_facebook_username(facebook_profile_link):
    '''
    This function uses the regex defined in 'pattern' variable to look for if the provided link is form a Facebook group feed.
    '''
    pattern = re.compile(r"(http|https):\/\/(web\.|www\.)facebook\.com\/(.+)\?fref=(nf|ufi)")
    match = pattern.search(facebook_profile_link)
    if match:

        # RegEx magic, baby ;)
        username = match.group(3)
        return username
