from django.shortcuts import render
from django.http import HttpResponse
from Photo_shop.models import Contact,Gallery
import random
# Create your views here.
def index(request):
    n= Gallery.objects.count()
    Images = list(Gallery.objects.all())
    Images = random.sample(Images,16)
    range1={"range": list, "images":Images,"count":n}

    return render(request,"index.html",range1)

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"services.html")
def contact(request):
    if request.method == "POST":
        print("post")
        name=request.POST.get("nav ")
        email = request.POST.get("email ")
        subject=request.POST.get("subject ")
        message =request.POST.get("message")
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,"contact.html")

def gallery(request):
    n= Gallery.objects.count()
    Images = list(Gallery.objects.all())
    Image = list(random.sample(Images,10))
    range1={"images":Images,"count":n ,"rand":Image}
    return render(request,"gallery.html",range1)
    
    
def cat(request):
    if request.method=="POST":
        Eng=request.POST.get("Engagement")
        haldi=request.POST.get("Haldi")
        wedding = request.POST.get("Wedding")
        d = {'a':Eng,'b':haldi,"c":wedding}
        for k,v in d.items():
            if d[k] is not None:
                pass1=Gallery.objects.filter(category=v)
                n = pass1.count()

                Pass = {"images":pass1,"count":n, "cate":v}
        return render(request,"Category.html",Pass)
    
    

def gs(request):
    return render(request,"gallery-single.html")