from django.db import models

class Chatbot(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)