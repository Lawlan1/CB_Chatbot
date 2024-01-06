
from django.contrib import admin
from django.urls import path, include
from chat.views import home, chatbot, history
from django.conf.urls.static import static
from django.conf import settings
from simple_chatbot.views import SimpleChatbot
from user_app.views import user_login
from chat import views
from chat.views import user_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_login, name='login'),
    path('user/', include('user_app.urls')),
    #path('', home, name='home'),
    path("simple_chatbot/", SimpleChatbot.as_view()),
    path('', chatbot, name='chatbot'),
    path('history/', views.history, name='history'),
    path('resources/', views.resource_list, name='resource_list'),
    path('feedback/', user_feedback, name='user_feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
