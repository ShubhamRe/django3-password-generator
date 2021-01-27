from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def home(request):
    #return HttpResponse("Hello there friends...!!!")
    return render(request,'generator/home.html',{'FirstName':'Shubham','MiddleName':'Sanjay','LastName':'Relekar'})

def password(request):
    genratedPassword = ''
    lowercasechars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        lowercasechars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('spChars'):
        lowercasechars.extend(list('~!@#$%^&*()_+:<>?/|,.'))
    if request.GET.get('numbers'):
        lowercasechars.extend(list('0123456789'))

    for x in range(int(request.GET.get('length'))):
        genratedPassword += random.choice(lowercasechars)

    return render(request, 'generator/passwords.html',{'password':genratedPassword})

def aboutUs(request):
    return render(request,'generator/aboutus.html')