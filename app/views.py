from django.shortcuts import render

# Create your views here.

def texttask(request):
    return render(request,'texttask.html')