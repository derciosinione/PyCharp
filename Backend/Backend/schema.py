import graphene
from User.schema import Query

class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)