
from graphene import (ObjectType,List, JSONString, String,
                     Field, Schema)
from graphene_django import DjangoObjectType
from GithubApiClient.base import query_resolver

#GraphQL types
class SearchType(ObjectType):
    items = List(JSONString)
    total_count = String()

#GraphQL query
class Query(ObjectType):
    search = Field(SearchType,name = String(required=True),
                                    language = String(),
                                    order = String(),
                                    sort = String(),
                                    per_page = String(),
                                    )

    def resolve_search(root,info,**kwargs):
        #validate field arguments
        params = {key:value.split('/')[-1].split('.')[0] for key, value in kwargs.items()
                                                    if len(value.strip(" ")) != 0 }
        del kwargs
        items, total_count = query_resolver(info=info,**params)
        return {'items' : items,'total_count':total_count}

schema = Schema(query=Query)
