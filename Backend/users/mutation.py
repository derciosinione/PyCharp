from graphql_jwt.decorators import permission_required, login_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_relay import from_global_id
from graphene import (
        ClientIDMutation, 
        relay, 
        Mutation, 
        ObjectType,
        ID,
        String,
        Field,
    )

from .geralImports import DsRelayFormMutation, user_verification

from .models import User, Profile, NetworkCredential
from .query import NetworkCredentialType, UserType, ProfileType
from .forms import UserForm


class UserMutation(DsRelayFormMutation):
    """
    Creating and Updating Users.
    This method create and update the Users
    When id field is informed it update de related data object, otherwise a new user is created.
    """
    class Meta:
        form_class = UserForm

    user = Field(UserType)
    
    # @login_required
    def perform_mutate(form, info):
        user = form.save()
        return UserMutation(user=user)


class RemoveUser(relay.ClientIDMutation):
    class Input:
        id = ID(required=True)

    user = Field(UserType)

    @classmethod
    @permission_required('auth.delete_user')
    def mutate_and_get_payload(cls, root, info, id):
        user = User.objects.get(pk=from_global_id(id)[1])
        user.delete()
        return RemoveUser(user=user)  


class NetworkCredentialMutation(relay.ClientIDMutation):
    """
    Creating and Updating Network Credential.
    This method create and update Network Credential
    When id field is informed it update de related data object, otherwise a new Network Credential is created.
    """
    
    class Input:
        id = ID()
        social_network = String(required=True)
        username = String(None)
        email = String(None)
        link = String(None)
        password = String(None)
    
    data = Field(NetworkCredentialType)
    
    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **Input):
        id = Input.get('id')
        social_network = Input.get('social_network')
        username = Input.get('username')
        email = Input.get('email')
        link = Input.get('link')
        password = Input.get('password')

        # user = User.objects.get(pk=from_global_id(Input.get('user'))[1])
        user = info.context.user
        
        # Add
        if id is None:
            data = NetworkCredential(social_network=social_network,username=username,email=email, link=link, password=password, user=user)
        else: #Edit
            data = NetworkCredential.objects.get(pk=from_global_id(id)[1])
            
            # verify if the user trying to perform this actions is the owner
            user_verification(data.user,user)
            
            data.social_network = social_network
            data.username = username
            data.email = email
            data.link = link
            data.password = password
            
        data.save()
        return NetworkCredentialMutation(data=data) 


class RemoveNetworkCredential(relay.ClientIDMutation):
    class Input:
        id = ID(required=True)

    post = Field(NetworkCredentialType)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, id):
        post = NetworkCredential.objects.get(pk=from_global_id(id)[1])
        
        user_verification(post.user,info.context.user)
        
        post.delete()
        return RemoveNetworkCredential(post=post)  


class Mutation(ObjectType):
    user = UserMutation.Field()
    remove_user = RemoveUser.Field()    
    
    networkCredential = NetworkCredentialMutation.Field()    
    remove_user = RemoveNetworkCredential.Field()    

