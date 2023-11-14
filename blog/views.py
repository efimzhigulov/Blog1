from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

def home(request):
    data = Articles.objects.all()
    context = {'data': data}
    return render(request, 'main/index.html', context)

# Create your views here.
