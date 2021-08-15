"""
Below classes define GraphQl types.
Graphene calss graphene.ObjectType creates custom fields or types to provide
an abstraction between GithubAPI and external API (React-peek_forntend)
"""

import graphene # django std GraphQl library


# class implemts user details type
class DetailsType(graphene.ObjectType):

    company = graphene.String()
    location = graphene.String()
    email = graphene.Date()


# class implemts user type
class UserType(graphene.ObjectType):

    url = graphene.String()
    name = graphene.String()
    joined = graphene.Date()
    details = graphene.Field(DetailsType)
