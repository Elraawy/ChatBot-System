from django.shortcuts import render
from .models import Conservation
# Create your views here.
from chatbot.message.chat import get_message
from chatbot.message.train import append, train_net
import subprocess

def main(request):
    if request.method == 'POST':
        title = 'a'
        msg = request.POST.get("msg")
        response = get_message(msg)


        Conservation.objects.create(title=title, content=msg, response=response)

        if msg == 'clear':
            Conservation.objects.all().delete()
        # if conversations.count() > 0:
        #     r
        # else:
        #     return render(request, "chat.html", {"cons" : conversation})
        return render(request, "chat.html", {"cons" :  Conservation.objects.all()})
    else:
        return render(request, "chat.html", {'cons': []})

def train(request):
    if request.method == 'POST':
        tag = request.POST.get("tag")
        pattern = request.POST.get("pattern")
        response = request.POST.get("response")
        print("adding to ", tag)
        append([tag,pattern,response])
        train_net()
        return render(request, "success.html",{"data":[tag,pattern,response]})
    else:
        return render(request, "optimize.html")
def index(request):
    return render(request,"index.html")