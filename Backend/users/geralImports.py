from graphql_relay import from_global_id
from graphene_django.forms.mutation import DjangoModelFormMutation


class DsRelayFormMutation(DjangoModelFormMutation):
    class Meta:
        abstract = True

    @classmethod
    def get_form_kwargs(cls, root, info, **input):
            kwargs = {"data": input}
            
            pk = input.pop("id", None)
            if pk:
                _, raw_pk = from_global_id(pk)
                instance = cls._meta.model._default_manager.get(pk=raw_pk)
                kwargs["instance"] = instance
            return kwargs
        

def user_verification(modeldataUser, user):
    """[User Verification]
    you can use the convenient user_verification function which raises a PermissionDenied
    exception when the informed users are not equal each other.
    
    Args:
        modeldataUser ([object]): [It is related with the user in your specific model]
        user ([object]): [It is related with the authenticated user who made the request]

    Raises:
        Exception: [raises a PermissionDenied
    exception when the informed users are not equal each other.]
    
    Returns:
        [bollean]: [return True
    if the informed users are not equal each other.]
    """
    if modeldataUser != user:
        raise Exception("You do not have permission to perform this action!")
    return True

# class DsRelayFormMutation(DjangoModelFormMutation):          
#     class Meta:
#         abstract = True
        
#     @classmethod
#     def get_form_kwargs(cls, root, info, **input):
            
#             fields = ["id","user"]

#             c = 0
#             for i in fields:
#                 try:
#                     input[fields[c]] = from_global_id(input[i])[1]
#                 except:
#                     continue
#                 c +=1
        
#             kwargs = {"data": input}
#             return kwargs
    