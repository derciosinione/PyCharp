from datetime import date
from graphql_jwt.decorators import permission_required
from graphene import relay, ObjectType, ID, Field, String
from graphql_relay import from_global_id

from .geralImports import DsRelayFormMutation 
from .query import NetworkCredentialType, UserType
from .forms import User, NetworkCredential, UserForm, NetworkCredentialForm


####### Usuarios
class UserMutation(DsRelayFormMutation):
    # """
    # Creating and Updating Users.
    # This method create and update the Users
    # When id field is informed it update de related data object, otherwise a new user is created.
    # """
    class Meta:
        form_class = UserForm

    user = Field(UserType)
    
    # @login_required
    def perform_mutate(form, info):
        user = form.save()
        return UserMutation(user=user)



class NetworkCredentialMutation(DsRelayFormMutation):
    class Meta:
        form_class = NetworkCredentialForm

    data = Field(NetworkCredentialType)
    
    # @login_required
    def perform_mutate(form, info):
        print(info.context.user)
        # data = None
        form.instance.user = info.context.user
        # form.instance.user = User.objects.get(pk=1)
        data = form.save()
        return NetworkCredentialMutation(data=data)


class CredentialMutationMotation(relay.ClientIDMutation):
    
    class Input:
        social_network = String(None)
        
    credential = Field(NetworkCredentialType)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **Input):
        social = Input.get('social_network')

        # user = User.objects.get(pk=from_global_id(Input.get('user'))[1])
        user = info.context.user
        print(user)
        credential = NetworkCredential.objects.get(pk=14)
        return CredentialMutationMotation(credential=credential) 


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

class RemoveNetworkCredential(relay.ClientIDMutation):
    class Input:
        id = ID(required=True)

    networkCredential = Field(UserType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        networkCredential = NetworkCredential.objects.get(pk=from_global_id(id)[1])
        networkCredential.delete()
        return RemoveUser(networkCredential=networkCredential)  


class Mutation(ObjectType):
    user = UserMutation.Field()
    remove_user = RemoveUser.Field()
    
    credential = NetworkCredentialMutation.Field()
    dsTeste = CredentialMutationMotation.Field()
    # remove_networkCredential = RemoveNetworkCredential.Field()

