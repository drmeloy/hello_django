# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

# def home(request):
#   return HttpResponse("Hello, Django!")

import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
      request,
      'hello/hello_there.html',
      {
        'name': name,
        'date': datetime.now()
      }
    )