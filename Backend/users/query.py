from graphene import relay, ObjectType, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .filerTypes import PostFilter, UserFilter, NetworkCredentialFilter
from .models import Post, User, NetworkCredential


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filterset_class = UserFilter 
        exclude = ('password',)
        interfaces = (relay.Node,)
    
    full_name = String()

    def resolve_full_name(self, info):
        return '%s %s' % (self.first_name, self.last_name)


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        filterset_class = PostFilter
        interfaces = (relay.Node,)
        
    picture_url = String()
    
    def resolve_picture_url(self, info):
        if self.picture:
            return self.picture.url
        return None


    
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
    
    post = relay.Node.Field(PostType)
    all_post = DjangoFilterConnectionField(PostType)
    
    # @login_required
    # @superuser_required
    def resolve_all_post(self, info, **kwargs):
        pass
    
