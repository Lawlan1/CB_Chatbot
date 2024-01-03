from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    USER = 'user'
    BOT = 'bot'

    SENDER_CHOICES = [
        (USER, 'User'),
        (BOT, 'Bot'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=4, choices=SENDER_CHOICES, default=USER)
    session = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Bot'} - {self.message} - {self.session}"


class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    attached_file = models.FileField(upload_to='resource_files/', null=True, blank=True)
    url_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
