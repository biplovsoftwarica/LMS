from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def home(request):
    return render(request,"homebase/base.html")