from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphene import relay, ObjectType
from .models import NetworkCredential
from .filterTypes import NetworkCredentialFilter

class NetworkCredentialType(DjangoObjectType):
    class Meta:
        model = NetworkCredential
        filterset_class = NetworkCredentialFilter
        interfaces = (relay.Node,)    
    
class Query(ObjectType):
    credential = relay.Node.Field(NetworkCredentialType)
    all_credential = DjangoFilterConnectionField(NetworkCredentialType)
    
    # @login_required
    # @superuser_required
    def resolve_all_post(self, info, **kwargs):
        pass