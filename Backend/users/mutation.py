from graphql_jwt.decorators import permission_required
from graphene import relay, ObjectType, ID, Field
from graphql_relay import from_global_id

from .geralImports import DsRelayFormMutation 
from .query import NetworkCredentialType, UserType
from .forms import User, NetworkCredential, UserForm, NetworkCredentialForm


####### Usuarios
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


class NetworkCredentialMutation(DsRelayFormMutation):
    """
    Creating and Updating NetworkCredential.
    This method create and update the NetworkCredential
    When id field is informed it update de related data object, otherwise a new NetworkCredential is created.
    """
    class Meta:
        form_class = NetworkCredentialForm

    credential = Field(NetworkCredentialType)
    
    # @login_required
    def perform_mutate(form, info):
        credential = form.save()
        return UserMutation(credential=credential)


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
    
    networkCredential = NetworkCredentialMutation.Field()
    remove_networkCredential = RemoveNetworkCredential.Field()

