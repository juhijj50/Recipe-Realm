from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
    {'name': 'Abhijeet Gupta', 'age': 26},
    {'name': 'Rohan Sharma', 'age': 23},
    {'name': 'Vicky Kaushal', 'age': 17},
    {'name': 'Deepanshu chaurasiya', 'age': 16},
    {'name': 'Sandeep', 'age': 63}
    ]
    for people in peoples:
        print(people)
    
    return render(request ,"home/index.html",context={'page':'2024 Django','peoples':peoples})

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html",context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html",context)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page.</h1>")