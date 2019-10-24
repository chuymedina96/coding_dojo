from __future__ import unicode_literals
from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class RegisterManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['username']) < 5:
            errors["username"] = "Username should be at least 5 characters."
        if len(postData['email_reg']) == 0:
            errors["email_reg_blank"] = "Please enter your email address."
        elif not email_regex.match(postData['email_reg']):
            errors["email_reg_invalid"] = "Please enter a valid email address."
        if len(User.objects.filter(email=postData['email_reg'])) > 0:
            errors["email_in_use"] = "Email already in use. Please log in."
        if len(postData['password_reg']) < 5:
            errors["pword_reg_short"] = "Password should be at least 5 characters."
        elif postData['password_reg'] != postData['password_confirm']:
            errors['pword_reg_match'] = 'Passwords do not match.'
        return errors

    def log_validator(self, postData):
        errors = {}
        if len(postData['email_log']) == 0:
            errors["email_log"] = "Please enter your email address."
        elif not email_regex.match(postData['email_log']):
            errors["email_log_invalid"] = "Please enter a valid email address."
        if len(postData['password_log']) < 5:
            errors["pword_log_short"] = "Password should be at least 5 characters."
        return errors

class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegisterManager()
    def __repr__(self):
        return f'<User object: ID ({self.id}) USERNAME {self.username}>'