from django.contrib import admin
from .models import ChatMessage, Resource


admin.site.register(ChatMessage)
admin.site.register(Resource)
admin.site.site_header = 'Chatbot Administration'

# Register your models here.

