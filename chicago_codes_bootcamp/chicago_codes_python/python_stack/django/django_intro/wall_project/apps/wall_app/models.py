from __future__ import unicode_literals
from django.db import models
from apps.log_reg.models import User

class MessageManager(models.Manager):
    def msg_validator(self, postData):
        errors = {}
        if len(postData['message']) < 5:
            errors["message"] = "Message should be at least 10 characters."
        return errors

    def cmt_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 5:
            errors["comment"] = "Comment should be at least 10 characters."
        return errors

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name='messages')
    likes = models.ManyToManyField(User, related_name='message_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
    def __str__(self):
        return f'<Message object: ID ({self.id}) TEXT {self.text}>'

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')
    likes = models.ManyToManyField(User, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
    def __str__(self):
        return f'<Message object: ID ({self.id}) TEXT {self.text}>'