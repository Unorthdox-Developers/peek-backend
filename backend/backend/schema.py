
"""

Unlike a RESTful API, there is only a single URL from which GraphQL is accessed.
Requests to this URL are handled by Graphene’s GraphQLView view.

"""

import graphene # django std GraphQl library
from DataEntry.githubAPI import UserInfo
from DataEntry.types import *

#Query
class Query(graphene.ObjectType):

    user = graphene.Field(UserType, user_id=graphene.String())

    def resolve_user(root,info,user_id):
        obj = UserInfo(user_id)
        return obj.get_json()

schema = graphene.Schema(query=Query)
