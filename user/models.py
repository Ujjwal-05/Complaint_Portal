from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stream = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=20)
    phone = models.IntegerField()
    enroll_no = models.CharField(max_length=10)
    session = models.IntegerField()

    def __str__(self):
        return self.user.email

