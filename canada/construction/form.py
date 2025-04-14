from .models import ContactForm as ContactFormModel
from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model =  ContactFormModel
        fields = ['name','number', 'comment']




class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',}),
        label=""
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',}),
        label=""
    ) 

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match")
        return cleaned_data        
    
    
 
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels= {
            'content':'To leave a review, you must first register on the main page and enter your login',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review...'})
        }
  
  
  
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=""
    )
        
        
        
    class Meta:
        model = User
        fields = ['username', 'password']
    