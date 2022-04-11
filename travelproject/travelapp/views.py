from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . models import place
from . models import members
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=members.objects.all()

    return render(request,"index.html",{'res':obj,'result':obj1})

