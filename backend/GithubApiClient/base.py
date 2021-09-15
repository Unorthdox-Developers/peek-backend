
"""
GithubApiClient is a REST api interface, which handles requests &
                responses between GraphQL client and github REST api
"""

from .api_callers import *

def query_resolver(info=None,*args,**kwargs):

    #dict stores GraphQL request query field with associated Github API
    request_path_mapper = {'search':SearchRepositories}
    if request_path_mapper.get(info.path[0],None):
        query_field = info.path[0]
        data = request_path_mapper[query_field](payload = kwargs)
        return data.parser()

    else:
        raise Exception("Query not found, please re-verify GraphQL request field")
