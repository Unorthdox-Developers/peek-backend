# coding utf-8
# Author: vinay

"""
Classes below responsible for returning rest api data from Github
"""


__all__ = ['SearchRepositories']

import requests
import reprlib

# cls returns a list of github repository json objects
class SearchRepositories(object):

    """
    url is an endpoint for a resource search/repositories and item_keys represent
    look_up keys to collect values from each search from items list
    """

    url = "https://api.github.com/search/repositories"
    item_keys = {'full_name', 'login', 'avatar_url','type','size','stars','forks','watchers',
                  'open_issues','description', 'created_at','updated_at', 'language','spdx_id',
                  'homepage','has_issues','default_branch'}

    def __init__(self,payload = None):

        self._items = []
        self._payload = None

        # reuest payload validation & verification
        if not self._payload and isinstance(payload,dict):
            self._payload = {**{ 'q':v for k,v in payload.items() if k =='name'},
                            **{k:v for k,v in payload.items() if k!='name'}}

    @property
    def items(self):
        return self._items

    @property
    def payload(self):
        return self._payload

    def __str__(self):
        return "object {0} with payload {1}".format(self.__class__.__name__,self.payload)

    def __repr__(self):
        items = reprlib.repr(self._items)
        return "SearchRepositories({0})".format(items)

    def __len__(self):
        return len(self._items)

    #HTTP get request
    def request_data(self):
        return requests.get(self.url,params=self._payload)

    # method maps values from github search api to item_keys
    def object_maker(self,keys,data):
        return { key:data.get(key,None) for key in keys }

    # github repositories search api parser
    def parser(self):

        data = self.request_data().json() # make a get request
        total_repos = {"total_repos":data.get("total_count",None)}
        api_data = data.get('items',None)

        #iterates each repository from items list and organize data
        for obj in api_data:
            user = obj.pop('owner',None)
            data_dict = None

            if obj.get('license',None):
                license = obj.pop('license',None)
                data_dict = {**obj,**user,**license}
            else:
                data_dict = {**obj,**user}

            self._items.append(self.object_maker(self.item_keys,data_dict))
        return (self.items, total_repos)
