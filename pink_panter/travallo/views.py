from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def view(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')