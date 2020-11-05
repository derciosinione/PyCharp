import graphene
from .models import NetworkCredential


class 

class Query(graphene.ObjectType):
    pass
    
schema = graphene.Schema(query=Query)