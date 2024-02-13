from django.shortcuts import render
from home.forms import RequestForm

def home(request):
    return render(request, 'home/home.html') 

def about(request):
    return render(request, 'home/about.html') 

def contact(request):
    return render(request, 'home/contact.html') 

def faq(request):
    return render(request, 'home/faq.html') 

def get_request(request):
    form = RequestForm()
    return render(request, 'home/get_request.html', {'form': form}) 


