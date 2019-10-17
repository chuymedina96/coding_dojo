from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show name should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Network Should be Longer than that"
        if len(postData['release']) < 2:
            errors["release"] = "Release date Should be Longer than that"
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description should be greater than 10 character"

        return errors


class Show(models.Model):
    title           = models.CharField(max_length=255)
    network         = models.CharField(max_length=255)
    release         = models.DateTimeField()
    desc            = models.CharField(max_length=255, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    objects         = ShowManager()

    def __repr__(self):
        return f" ID: {self.id}, Show: {self.title}, Network {self.network}"

    