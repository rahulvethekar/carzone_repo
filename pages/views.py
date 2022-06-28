from django.http import HttpResponse
from django.shortcuts import render
from django.http import response
# Create your views here.
def home(request):

    #return HttpResponse('<h1>welcome!</h1>')
    return render(request,'pages/home.html') 