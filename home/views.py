from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html') 

def about(request):
    return render(request, 'home/about.html') 

def contact(request):
    return render(request, 'home/contact.html') 

def faq(request):
    return render(request, 'home/faq.html') 

def get_request(request):
    return render(request, 'home/get_request.html') 


