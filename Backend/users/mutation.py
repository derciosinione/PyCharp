from graphql_jwt.decorators import permission_required
from graphene import relay, ObjectType, ID, Field
from graphql_relay import from_global_id

from .geralImports import DsRelayFormMutation 

from .models import User
from .query import UserType
from .forms import UserForm

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


class Mutation(ObjectType):
    user = UserMutation.Field()
    remove_user = RemoveUser.Field()
