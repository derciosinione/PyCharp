
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, String, ObjectType

from .filerTypes import NetworkCredentialFilter, UserFilter
from .models import User, NetworkCredential, Profile


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filterset_class = UserFilter 
        exclude = ('password',)
        interfaces = (relay.Node,)
    
    full_name = String()
    picture = String()

    def resolve_full_name(self, info):
        return '%s %s' % (self.first_name, self.last_name)
    
    def resolve_picture_url(self, info):
        return self.profile.picture.url


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = {
            'user': ['exact'],
        }
        # convert_choices_to_enum = False
        interfaces = (relay.Node,)


class NetworkCredentialType(DjangoObjectType):
    class Meta:
        model = NetworkCredential
        filterset_class = NetworkCredentialFilter 
        interfaces = (relay.Node,)
    

class Query(ObjectType):
    user = relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)
    
    profile = relay.Node.Field(ProfileType)
    all_profiles = DjangoFilterConnectionField(ProfileType)
    
    networkCredential = relay.Node.Field(NetworkCredentialType)
    all_networkCredentials = DjangoFilterConnectionField(NetworkCredentialType)
    