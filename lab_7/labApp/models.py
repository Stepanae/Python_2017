from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=75)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.user)


class Departments(models.Model):
    department_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} {}".format(self.department_name, self.description)