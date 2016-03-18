from django.shortcuts import render
from .models import Log_list

# Create your views here.

def home(request):
    entry_log = Log_list.objects.all()
    return render(request, 'home.html', {'entry_log': entry_log})