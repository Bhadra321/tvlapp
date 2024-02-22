from django.shortcuts import redirect, render
from .models import Apartment
from django.http  import HttpResponse
from django.contrib.auth.models import User,AbstractUser
from .models import Users,Register
from django.contrib import messages

# Create your views here.
def sample(request):
    api=Apartment.objects.all()
    return render(request, 'index.html',{'data1':api})
# def register(request):
#     if request.method== 'POST':
#         uname = request.POST['uname']
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         em=request.POST['ema']
#         passw=request.POST['pass']
#         cpass=request.POST['cpass']
#         pho=request.POST['phone']
#         pla=request.POST['place']
#         if passw==cpass:
#            user=User.objects.create_user(username=uname,password=passw,first_name=fname,last_name=lname,email=em)
#            Users.objects.create(phone=pho,place=pla,user_id=user.id)


#            user.save()
#            print("got it")
#            return HttpResponse("sucesssssssssssssss")
#     else:
#       print("password incorect")

#       return render(request, 'register.html')




# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render

# 
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            request.session['user']=user.id
            messages.info(request,'invalid credentials')
            return redirect('login')
        else:
             messages.info(request,'sucessfull')
             return redirect('sample')
    else:
      return render(request,"login.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        regno=request.POST['regno']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if Register.objects.filter(username=username).exists():
                messages.warning(request,"Username already exists")
                return redirect(register)
            elif Register.objects.filter(regno=regno).exists():
                messages.warning(request,"Registration number already exists")
                return redirect(register)
            else:
                user=Register.objects.create(firstname=firstname,lastname=lastname,age=age,
                                           gender=gender,email=email,regno=regno,
                                           phone=phone,username=username,password=password,Value=0,user_type='student')
                user.save()
                messages.info(request,'User Added')
                return redirect('login')
        else:
           messages.info(request,"password not matched")
    return render(request,'registration.html')

