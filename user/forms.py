from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
STREAM_CHOICES =(
    ("Computer Science And Engieering", "CSE"),
    ("Infornation Technology", "IT"),
    ("Electrical And TeleCommunication", "E&TC"),
    ("Mechanical", "Mech"),
    ("Civil", "Civil"),
)

GENDER_CHOICES =(
    ("Male", "Male"),
    ("Female", "Female"),
)

class UserForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    stream=forms.ChoiceField(choices=STREAM_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    enroll_no = forms.CharField(max_length=10)
    session = forms.IntegerField()
    email=forms.EmailField()
    password = forms.CharField(max_length=20)

class AdminForm(UserCreationForm):
       class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','is_superuser','is_staff']