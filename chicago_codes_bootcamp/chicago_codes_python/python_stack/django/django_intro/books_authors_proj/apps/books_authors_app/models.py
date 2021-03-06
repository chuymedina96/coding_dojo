from django.db import models

# Create your models here.
class Author(models.Model):
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    notes       = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Author: {self.firstName}, {self.lastName}"

class Book(models.Model):
    title       = models.CharField(max_length=255)
    desc        = models.CharField(max_length=255, null=True)
    author      = models.ManyToManyField(Author, related_name="books", null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __repr__(self):
        boop = self.author.all()
        # if self.author.all() == None:
        #     return f"Book: {self.title}, Author: None"
        # else:
        return f"Book: {self.title} Author: {boop} ID: {self.id}"
