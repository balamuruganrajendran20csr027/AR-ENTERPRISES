from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from django.contrib import messages
from .models import Scrap,Enquirie

def home(request):
    data=Scrap.objects.all()
    print(data)
    return render(request,"home.html",{"data":data})

def enquiry(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        companyname=request.POST.get("companyname")
        contactnumber=request.POST.get("contactnumber")
        address=request.POST.get("address")
        gst=request.POST.get("gst")
        comments=request.POST.get("comments")
        feed=Enquirie(name=name,email=email,companyname=companyname,contactnumber=contactnumber,address=address,gst=gst,comments=comments)
        feed.save()
        messages.success(request, "Enquiry form submitted successfully")
        return redirect("home")
    else:
        messages.warning(request, "Error while submitted the form")
        return redirect("home")
