from django_filters import FilterSet, OrderingFilter
from .models import NetworkCredential


class NetworkCredentialFilter(FilterSet):
    class Meta:
        model = NetworkCredential
        fields = '__all__'
    
    filter_fields = {
            'social_network': ['exact', 'icontains', 'istartswith'],
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'user': ['exact',],
         }
    
    order_by = OrderingFilter(
        fields = (
            # field and de argument
            ('id','id'),
            ('title','title'),
            ('username','username'),
            ('dateCreated', 'dateCreated'),
        )
    )
