from django.shortcuts import render, HttpResponse
from club import models
from club.models import Resister
# Create your views here.
def club(request):
   # return HttpResponse("This is bjtfh")
   return render(request,'home.html')

def base(request):
  #  return HttpResponse("THis is resister")
   return render(request,'base.html')



def gallery(request):
   # return HttpResponse("THis is gallery")
    return render(request,'gallery.html')

def ourteam(request):
    #return HttpResponse("THis is ourteam")
     return render(request,'ourteam.html')

def resister(request):
   if request.method=="POST":
      print("this is post")
      name=request.POST['name']
      school=request.POST['school']
      phone=request.POST['phone']
     # print(name,city,phone)
      resister=Resister(name=name,school=school,phone=phone)
      resister.save()
      print("this data has been written to the db")
  # return HttpResponse("THis is resister")
   return render(request,'resister.html')

   