from django.shortcuts import render

def home(request):
    return render(request, 'tutorial/home.html')

def recipes(request):
    return render(request, 'tutorial/recipes.html')

def about(request):
    return render(request, 'tutorial/about.html')

def contact(request):
    return render(request, 'tutorial/contact.html')
