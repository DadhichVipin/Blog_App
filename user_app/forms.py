from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'user', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter THe Title'}),
             'user': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'auth', 'type':'hidden'}),
            # 'user': forms.Select(attrs={'class':'form-control', 'value':'', 'id':'auth'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter What You Want'})
        }


class CreateUsers(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')
