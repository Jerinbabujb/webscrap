from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from .models import weblink

# Create your views here.
def home(request):
    if request.method=='POST':
        h=request.POST.get('gl')
        ur=requests.get(h)
        beauti=BeautifulSoup(ur.text,'html.parser')
        for i in beauti.find_all('a'):
            lin=i.get('href')
            nam=i.string
            a=weblink(name=nam,lin=lin)
            a.save()
    bi=weblink.objects.all()
    return render(request,'home.html',{'b':bi})


