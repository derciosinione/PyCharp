from django import forms
from .models import NetworkCredential 


class NetworkCredentialForm(forms.ModelForm):    
    class Meta:
        model = NetworkCredential
        # fields = ['title','content','user'] 
        fields = '__all__' 
