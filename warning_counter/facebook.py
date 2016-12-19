'''
The whole purpose in life of this file is to handle various stuff related to facebook and this project.
'''

import re


def get_facebook_username_or_id(facebook_profile_link):
    '''
    This function uses the regex defined in 'pattern' variable to look for if the provided link is form a Facebook group feed.
    '''

    pattern = re.compile(r"(http|https):\/\/(web|www|m|mobile|touch|mbasic|iphone|free)\.facebook\.com\/((.+)\?fref=(nf|ufi)|profile\.php\?id=([0-9]{15}))")
    match = pattern.search(facebook_profile_link)
    if match:

        # RegEx magic, baby ;)
        if match.group(4):
            username = match.group(4)
            return username
        elif match.group(6):
            userid = match.group(6)
            return userid
        else:
            return None
