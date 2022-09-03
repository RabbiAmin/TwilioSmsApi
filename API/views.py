from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client

from . models import Compliment
from .forms import complimentForm



def broadcast_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")
    client = Client('XXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXX')
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=+111111111,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)

def get_sent_messages():
     messages = []
     return messages

#Create your views here.
def Compliment(request):
     page = 'home'
     if request.method == 'POST':
        form = complimentForm(request.POST)
        if form.is_valid():
            now=datetime.now()
            number=request.POST['number']
            sender = request.POST['sender']
            compliment = request.POST['compliment']
            create_msg = Compliment.objects.create(number= number, sender = sender, compliment = compliment, ctime=now)
            messages.success(request, "Your message has been submitted successfully!!!")
            return redirect("Compliment")
     else:
        form = complimentForm()
     return render (request, page + ".html", {'form': form})





# # Create your views here.
# def index(request):
#     page = 'home'
#     messages = get_sent_messages()
#     return render (request, page + ".html")

# def get_sent_messages():
#     messages = []
#     return messages

# def send_message(to,body):
#     pass

# def add_compliment():
#     sender = request.values.get('sender','Someone')
#     receiver = request.values.get('receiver', 'Someone')
#     compliment = request.values.get('compliment', 'wonderful')
#     to = request.values.get('to')
#     body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
#     send_message(to, body)
#     print('Your message was successfully sent')
#     return redirect('index')



