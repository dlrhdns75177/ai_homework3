from django.shortcuts import render,redirect
from .main import chatbot_response
from .models import Chatbot

def chatbot(request):
    if request.method =="POST":
        user_message = request.POST.get("message","")

        assistant_reply = chatbot_response(user_message)

        Chatbot.objects.create(user_message=user_message, bot_message=assistant_reply)

        chat = Chatbot.objects.all().order_by('-pk') 
        context = {
            "chat":chat,
            "user_message":user_message,
            "bot_reply":assistant_reply
        }
        return render(request, "chatbot/chatbot.html", context)
    
    else:
        chat = Chatbot.objects.all().order_by('-pk')
        context = {
            "chat":chat
        }
        return render(request, "chatbot/chatbot.html", context)