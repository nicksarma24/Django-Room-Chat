from django.db import models #here db is module and models is a class, Contains Model class + fields + helper functions
from django.contrib.auth.models import User
#contrib is moduel which Contains optional “contributed” modules (like auth, admin, sessions)
#models is moduel Contains model classes related to auth, including User
#User is class, its a built-in Django model class representing a user in the database


class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
#__str__ is a special method in a Django model that tells Python how to display the object as a string.
#When you print() the object or see it in Django admin, it will show self.name instead of <Student object>. Makes objects readable and meaningful.

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]   #trimming the body is the messgae is too long
