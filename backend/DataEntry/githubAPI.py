
"""
Below implentation requests github user's profile and and repository information
using API https://api.github.com (version v3)
"""

from datetime import date
import requests # HTTPS library
import functools

# class implements github user api resource
class UserInfo:

    def __init__(self,username):
        self.username = username
        self.data = self.get_user_object().json()
        self.status_code = self.get_user_object().status_code

    # make api call
    @functools.lru_cache() # last recently used cache decorator
    def get_user_object(self):

        github_api = 'https://api.github.com'
        url = '{0}/users/{1}'.format(github_api,self.username)
        data = requests.get(url)
        return data

    #date formater
    def format_date(self,date_string):
        return date.fromisoformat(date_string.split('T')[0])

    # GraphQL user type
    def usr_details(self):
        details = {
                    'company': self.data.setdefault('company',None),
                    'location' : self.data.setdefault('location',None),
                    'email' : self.data.setdefault('email',None),
        }
        return details

    # GraphQL user root
    def usr_profile(self):
        if self.status_code == 200:

            profile = {
                    'name': self.data.setdefault('name',None),
                    'url' : self.data.setdefault('html_url',None),
                    'joined' : self.format_date(self.data.setdefault('created_at',None)),
                    'details' : self.usr_details()
                    }
            return profile

        else:
            return Exception("username {0} not found in github, \
                            please verify!".format(self.username))

    # return user data to GraphQL schema
    def get_json(self):
        user_obj = self.usr_profile()
        return user_obj
