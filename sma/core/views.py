from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # this needs to be fixed for some reason it is not working.
    return render(request, 'index.html')
    #return HttpResponse('<h1>Welcome to our Social Media Application!</h1>')