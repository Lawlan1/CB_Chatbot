from django.contrib import admin
from .models import ChatMessage, Resource, UserFeedback


admin.site.register(ChatMessage)
admin.site.register(UserFeedback)
admin.site.register(Resource)
admin.site.site_header = 'Chatbot Administration'

# Register your models here.

