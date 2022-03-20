from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        option = request.POST.get("budget")
        name = str(name)
        email = str(email)
        phone = str(phone)
        message = str(message)
        if option == "Local Storage":
            file1 = open("LOCALFILE.text","w")
            l = [name,email,phone,message]
            file1.writelines(l)
            res = "Saved to local storage"
            return render(request,"index.html",{'res':res})
        elif option == "MySQL Database":
            data = contact_DB(name=name,email=email,phone=phone,message=message)
            data.save()
            res = "Saved to MySQL Database"
            return render(request,"index.html",{'res':res})
    
    return render(request,"index.html")

        