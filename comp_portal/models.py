from django.db import models
from django.contrib.auth.models import User
#from Greviance_System.user.models import  Userprofile
PROBLEM_TYPE =(
    ("Ragging", "Ragging"),
    ("Administration", "Administration"),
    ("Faculty","Faculty"),
    ("Hostel","Hostel")
)

class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #stream=models.CharField(max_length=20)
    #gender=models.CharField(max_length=20)
    time=models.DateField(auto_now_add=True)
    type=models.CharField(max_length=20,choices=PROBLEM_TYPE)
    title=models.CharField(max_length=200)
    problem=models.TextField(max_length=5000)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
