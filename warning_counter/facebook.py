'''
The whole purpose in life of this file is to handle various stuff related to facebook and this project.
'''

import re

def is_facebook_link(link):
    '''
    This function uses the regex defined in 'pattern' variable to look for if the provided link is form a Facebook group feed.
    '''
    pattern = re.compile(r"(http|https):\/\/?(?:web.)?facebook.com\/.+\?+(fref)+=(nf|ufi)")
    match = pattern.search(link)
    if match:
        raw_link = match.group()
        # With HTTPS the part before the username is 25chars long.
        username_with_excess = raw_link[25:]
        username_chars = []

        # Loops through the string to find the username chars.
        for char in username_with_excess:
            if char != '?':
                username_chars.append(char)
            else:
                break
        username = ''.join(username_chars)
        return username
