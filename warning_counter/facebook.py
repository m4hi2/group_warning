'''
The whole purpose in life of this file is to handle various stuff related to facebook and this project.
'''

import re

def get_facebook_username(facebook_profile_link):
    '''
    This function uses the regex defined in 'pattern' variable to look for if the provided link is form a Facebook group feed.
    '''
    pattern = re.compile(r"(http|https):\/\/(web|www|m|mobile|touch|mbasic|iphone|free)\.facebook\.com\/(.+)\?fref=(nf|ufi)")
    match = pattern.search(facebook_profile_link)
    if match:

        # RegEx magic, baby ;)
        username = match.group(3)
        return username

def get_facebook_profile_ID(facebook_profile_link):
    '''
    :param facebook_profile_link: provided facebook profile link
    :return: facebook profile ID
    '''
    pattern = re.compile(r"(http|https):\/\/(web|www|m|mobile|touch|mbasic|iphone|free)\.facebook\.com\/profile\.php\?id=([0-9]{15})")
    match = pattern.search(facebook_profile_link)
    if match:
        # regex group
        user_id = match.group(3)
        return user_id
