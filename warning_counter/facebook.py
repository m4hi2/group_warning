'''
The whole purpose in life of this file is to handle various stuff
related to facebook and this project.
'''

import re


def get_fb_username_or_id(fb_profile_link):
    '''
    This function takes facebook profile link as parameter and returns
    the username or profile ID using regex if exits, otherwise returns None.

    >>> get_fb_username_or_id('https://www.facebook.com/fr070?fref=ufi')
    'fr070'
    >>> get_fb_username_or_id('https://www.facebook.com/profile.php?id=100001448059447&fref=ufi')
    '100001448059447'
    >>> print(get_fb_username_or_id('https://www.facebook.com/'))
    None
    '''

    pattern = re.compile(r"(http|https):\/\/(web|www|m|mobile|touch|mbasic|iphone|free)\.facebook\.com\/((.+)\?fref=(nf|ufi)|profile\.php\?id=([0-9]{15}))")
    match = pattern.search(fb_profile_link)
    if match:
        # If username is found
        if match.group(4):
            username = match.group(4)
            return username
        # So username has not been found, let's check profile ID
        if match.group(6):
            profile_id = match.group(6)
            return profile_id
    # Nothing matched :(
    return None
