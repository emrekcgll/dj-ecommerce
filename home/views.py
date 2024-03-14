from django.shortcuts import render
from home.forms import RequestForm, ContactForm

def home(request):
    return render(request, 'home/home.html') 

def about(request):
    return render(request, 'home/about.html') 

def contact(request):
    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form}) 

def faq(request):
    return render(request, 'home/faq.html') 

def get_request(request):
    form = RequestForm()
    return render(request, 'home/get_request.html', {'form': form}) 


