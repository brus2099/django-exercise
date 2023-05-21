from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def about(request):
  return render(request, 'generator/about.html')
  
def home(request):
  return render(request, 'generator/home.html')

def password(request):
  characteres = list('abcdefghijklmnopqrstuvwxyz')
  generated_password = ''

  length = int(request.GET.get('length'))
  if request.GET.get('uppercase'):
    characteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
  if request.GET.get('special'):
    characteres.extend(list('!@#$%&*()'))
  if request.GET.get('number'):
    characteres.extend(list('0123456789'))    

  for x in range(length):
    generated_password += random.choice(characteres)

  return render(request, 'generator/password.html', {'password': generated_password})