import graphene
import graphql_jwt
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated

from users.schema import Query as usersQuery, Mutation as usersMutation
from users.query import UserType


class ObtainJSONWebToken(graphql_jwt.relay.JSONWebTokenMutation):
    user = graphene.Field(UserType)
    
    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)                 


class Query(
    usersQuery,
    graphene.ObjectType):
    pass


class Mutation(
    usersMutation,
    graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.refresh_token.relay.DeleteRefreshTokenCookie.Field()

    #4.2.6 One time only use refresh token
    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)


schema = graphene.Schema(query=Query, mutation=Mutation)