from django.shortcuts import render
from django.http import HttpResponse
from .forms import takeInput

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html')

def home(response):
    if response.method == "POST":
        form = takeInput(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            device_ip = form.cleaned_data["device_ip"]
            self_ip = form.cleaned_data["self_ip"]
            peer_ip = form.cleaned_data["peer_ip"]
            self_AS = form.cleaned_data["self_AS"]
            remote_AS = form.cleaned_data["remote_AS"]
            device_select = form.cleaned_data["device_select"]
            return HttpResponse(str("Command sent successfully!"))
        else:
            return HttpResponse(str("Parameters not entered correctly!"))
    else:
        form = takeInput()
        return render(response, 'home.html', {'form': form})
    
