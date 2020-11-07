from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User, NetworkCredential


class UserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email'] 


class NetworkCredentialForm(forms.ModelForm):    
    class Meta:
        model = NetworkCredential
        # fields = ['user','social_network','username','email','link','password'] 
        exclude = ('user',)
        
        # def save(self, commit=True):
        #     self.instance
        
class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['title','content','user'] 
