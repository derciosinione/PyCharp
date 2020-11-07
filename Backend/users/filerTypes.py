from users.models import NetworkCredential
from django_filters import FilterSet, OrderingFilter

from .models import User, NetworkCredential

class UserFilter(FilterSet):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)
    
    filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
        }

    order_by = OrderingFilter(
            fields = (
                # field and de argument
                ('id','id'),
                ('username','username'),
                ('first_name','fullName'),
                ('email', 'email'),
                ('date_joined', 'dateJoined'),
            )
        )


class NetworkCredentialFilter(FilterSet):
    class Meta:
        model = NetworkCredential
        fields = '__all__'
        # exclude = ('password',)
    
    filter_fields = {
            'user': ['exact',],
            'social_network': ['exact', 'icontains', 'istartswith'],
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'link': ['exact', 'icontains', 'istartswith'],
            'dateCreated': ['exact', 'icontains', 'istartswith'],
        }

    order_by = OrderingFilter(
            fields = (
                # field and de argument
                ('id','id'),
                ('username','username'),
                ('social_network','social_network'),
                ('email', 'email'),
                ('dateCreated', 'dateCreated'),
            )
        )
