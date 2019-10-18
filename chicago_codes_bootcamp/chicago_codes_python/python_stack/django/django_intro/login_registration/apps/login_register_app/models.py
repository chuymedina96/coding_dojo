from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["firstName"]) < 2:
            errors["firstName"] = "User First Name should be at least 2 characters"
        if len(postData["lastName"]) < 2:
            errors["lastName"] = "User Last Name Should be Longer than that"
        if len(postData["email"]) < 2:
            errors["email"] = "email must be a valid email"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 character long"
        if postData["password"] != postData['confirm']:
            errors["password"] = "Password does not match. Try again"

        return errors


class User(models.Model):
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    email       = models.EmailField(max_length=255)
    password    = models.CharField(max_length=255)
    objects     = UserManager()

    def __repr__(self):
        return f" ID: {self.id}, Name: {self.firstName} {self.lastName}, Email: {self.email} Password: {self.password}"

