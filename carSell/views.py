from django.shortcuts import render , redirect
from product.models import product_info
from django.contrib import messages
from account.models import account
from userContactUs.models import userContacted


def home(request):
    product_detail = product_info.objects.all()
    data = {
        "product":product_detail
    }
    return render(request, "index.html",data)
def discover(request):
    product_detail = product_info.objects.all()
    data = {
        "product":product_detail
    }
    return render(request, "discover.html",data)
def secret(request):
    return render(request, "secret.html",data)
def contact(request):
    if request.method=="POST":
        fname = request.POST['fullname']
        email = request.POST['email']
        question = request.POST['question']
        user = userContacted.objects.create(fullname=fname,email=email,question=question)
        user.save()
        messages.info(request, "sent successfully")
    return render(request, "contact.html")


def register(request):
    if request.method=="POST":
        fname = request.POST['fullname']
        number = request.POST['number']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
           
            if len(password) >=8:
                if account.objects.filter(email=email).exists():
                    
                    messages.info(request, "email already exist please login.")
                    return render(request, "login.html")
                    
                else:
                    if account.objects.filter(number=number).exists():
                        messages.info(request, "number already exist.")
                        return render(request, "login.html")
                        
                    else:
                        user = account.objects.create(fullname=fname,number=number,email=email,state=state,city=city,password=password)
                        user.save()
                        return redirect('/login')
            else:
                messages.info(request, "password must be of 8 character")
                return render(request, "register.html")
             

        else:
            messages.info(request, "Please enter same password")
            return render(request, "register.html")
    else:
        return render(request, "register.html")
    return render(request, "register.html")
def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        if account.objects.filter(email=email).exists() and account.objects.filter(password=password).exists():
            product_detail = product_info.objects.all()
            data = {
                'user':account.objects.all().filter(email=email),
                "product":product_detail
            }
            return render(request,"secret.html", data)
        else:
            messages.info(request, "Invalid")
    return render(request, "login.html")