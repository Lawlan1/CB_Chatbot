from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatbotForm
from .models import ChatMessage, Resource
from django.contrib.sessions.models import Session
from django.db.models import Max, F, Count
from .forms import UserFeedbackForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')


@login_required
def history(request):
    session_id = request.GET.get('session')
    date_history = request.GET.get('date')
    print(date_history)
    chat_history = ChatMessage.objects.filter(session=session_id)
    latest_messages = ChatMessage.objects.filter(user__username=request.user).values('session').annotate(message_count=Count('message'), max_timestamp=Max('timestamp')).order_by('-max_timestamp')

    return render(request, 'history.html', {'date_history': date_history, 'chat_history': chat_history, 'latest_messages': latest_messages})


@login_required
def chatbot(request):
    output = None
    chat_history = []
    latest_messages = []  # Initialize with an empty list

    session_id = request.session.session_key

    # Retrieve session-specific chat history outside the POST block
    chat_history = ChatMessage.objects.filter(session=session_id).order_by('timestamp')
    latest_messages = ChatMessage.objects.filter(user__username=request.user).values('session').annotate(message_count=Count('message'), max_timestamp=Max('timestamp')).order_by('-max_timestamp')

    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            api_url = 'http://childbullyingsupport.azurewebsites.net/simple_chatbot/'
            headers = {'Content-Type': 'application/json'}
            data = {'message': user_message}

            try:
                response = requests.post(api_url, data=json.dumps(data), headers=headers)
                response_data = response.json()
                bot_message = response_data.get('message', '')
                
                # Save user and bot messages to the database
                user_chat = ChatMessage.objects.create(user=request.user, message=user_message, sender=ChatMessage.USER, session=session_id)
                bot_chat = ChatMessage.objects.create(user=request.user, message=bot_message, sender=ChatMessage.BOT, session=session_id)

                abs_list = [abs(x) for x in range(5)]  

                # Continue with your existing code
                min_abs = min(abs_list)
                output = bot_message
            except requests.RequestException as e:
                bot_message = "I don't understand your question, kindly rephrase"
                user_chat = ChatMessage.objects.create(user=request.user, message=user_message, sender=ChatMessage.USER, session=session_id)
                bot_chat = ChatMessage.objects.create(user=request.user, message=bot_message, sender=ChatMessage.BOT, session=session_id)

    else:
        form = ChatbotForm()

    return render(request, 'chatbot.html', {'form': form, 'output': output, 'chat_history': chat_history, 'latest_messages': latest_messages})



def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

@login_required
def user_feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user if request.user.is_authenticated else None
            feedback.save()
            messages.success(request, f'Feedback submitted successfully')
            previous_page = '/feedback/'
            return redirect(previous_page)
    else:
        form = UserFeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})

