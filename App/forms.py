from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import predmeti
from django.forms import ModelForm

#create forms here:

class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        User=get_user_model()
        model=User
        fields=("username","email","password1","password2")
    def save(self, commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class editForm(ModelForm):
    class Meta:
        model=predmeti
        fields=['ime','kod','program','bodovi','sem_redovni','sem_izvanredni','izborni']
        
class createForm(ModelForm):
    class Meta:
        model=predmeti
        fields=['ime','kod','program','bodovi','sem_redovni','sem_izvanredni','izborni']

class deleteForm(ModelForm):
    class Meta:
        model=predmeti
        fields=[]
