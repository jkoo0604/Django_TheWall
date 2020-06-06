from django.db import models
from datetime import datetime
from login.models import User

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=70)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

##    messages
##    usercomments

#     def __repr__(self):
#         return f"{self.first_name} {self.last_name} ({self.email})"

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #comments

class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name="usercomments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
