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