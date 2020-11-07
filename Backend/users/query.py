from graphene import relay, ObjectType, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .filerTypes import UserFilter, NetworkCredentialFilter
from .models import User, NetworkCredential


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filterset_class = UserFilter 
        exclude = ('password',)
        interfaces = (relay.Node,)
    
    full_name = String()

    def resolve_full_name(self, info):
        return '%s %s' % (self.first_name, self.last_name)
    
    
class NetworkCredentialType(DjangoObjectType):
    class Meta:
        model = NetworkCredential
        filterset_class = NetworkCredentialFilter 
        interfaces = (relay.Node,)
    

class Query(ObjectType):
    user = relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)
    
    credential = relay.Node.Field(NetworkCredentialType)
    all_credentials = DjangoFilterConnectionField(NetworkCredentialType)
