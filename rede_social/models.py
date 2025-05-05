from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return self.user.username


STATUS = {
    'SENDED':'SENDED',
    'REJECTED':'REJECTED',
    'APROVED':'APROVED'
}
import uuid
class Invite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.CharField(max_length=8, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    accept_at = models.DateTimeField(auto_now_add=True)

    
# class ChatRoom(models.Model):
#     name = models.CharField(max_length=255)
#     user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')

# ChatRoom.objects.filter('id+id2')

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     content = models.TextField()
#     created_at = models.DateTimeField()

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
#     content = models.TextField()
#     created_at = models.DateTimeField()

# from django.db.models import Q
# Message.objects.filter(Q(reciver=request.user) | Q(sender=request.user))