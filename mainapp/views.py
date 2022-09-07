import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest as request
from django.http import HttpResponse as response
from django.contrib.auth.models import User,auth

from .models import employee,service,product
import hashlib


def main(request):
      return render(request,'index.html')

def signup(request):
      if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('passwd')
            email=request.POST.get('email')
            if User.objects.filter(username=email).exists():
                   print("user name exist")
                   return render(request, "signup.html",{'messsage':'user with email already exists'})
            else:
                  user = User.objects.create_user(username=email,password=password,first_name=name)
                  user.save()
                  print("user created")
                  return redirect(login)
      else:
            message=None
            return render(request,"signup.html",{'messsage':message})
def login(request):
      if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('passwd')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                  auth.login(request, user)
                  return redirect(myaccount)
            else:
                  return render(request, 'login.html',{'message':"wrong username or password"})
      else:
            message=None
            return render(request, 'login.html',{'messsage':message})


def myaccount(request):
      user=auth.get_user(request)
      ser=service.objects.filter(customer_id=user.id)
      if ser.exists():
            pro=product.objects.filter(customer_id=user.id)
            if pro.exists():
                  print('here')
                  emp = employee.objects.filter(id =ser[0].employee_id)
                  return render(request,'home.html',{'messsage':1,'pro':pro[0],'emp':emp[0],'ser':ser[0]})
      else:
            return render(request,'home.html', {'message':0 })
def home(request):
      return render(request,'index.html')

def register(request):
      if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('passwd')
            phone ="+91"+str( request.POST.get('phone'))
            email=request.POST.get('email')
            q=request.POST.get('qualification')
            if employee.objects.filter( email=email).exists():
                   print("user name exist")
                   return render(request, "register.html",{"messsage":1 })
            else:
                  emp = employee.objects.create(username=username,
                                                password=hashlib.sha256(password.encode('utf-8')).hexdigest(),
                                                email=email,phone=phone,qualification=q)
                  emp.save()
                  print("user created")
                  return redirect(employees)
      else:
            message=0
            return render(request,'register.html',{'messsage':message})

def employees(request):
      if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('passwd')
            emp= employee.objects.filter(email=username,password=hashlib.sha256(password.encode('utf-8')).hexdigest())
            if emp.exists():
                  name=emp[0].username
                  print("the object is",name)
                  if service.objects.filter(employee_id=emp[0].id,done=False).exists():
                        ser=service.objects.filter(employee_id=emp[0].id,done=False)[0]
                        user=User.objects.get(id=ser.customer_id)
                        global cur_empuser
                        cur_empuser=ser.employee_id
                        if(ser.done==True):
                              message = 0
                              return render(request, 'emp_home.html', {'messsage': message, 'name': name})
                        pro=product.objects.get(customer_id=user)
                        return render(request,'emp_home.html',{'name':name,'message':1,'pro':pro,'user':user,'ser':ser})
                  else:
                        message=0
                        return render(request,'emp_home.html',{'messsage':message,'name':name})
            else:
                  return render(request, 'employee.html', {'message': "wronge username or password",})
      else:
            message = 1
            return render(request, 'employee.html',{'messsage': message})
def done(request):
    if request.method == 'POST':
       change=service.objects.get(employee_id=cur_empuser,done=False);
       change.done=True
       change.save()
       print(change.done)
       users=employee.objects.get(id=cur_empuser)
       message = 0
       return render(request, 'emp_home.html',{'messsage': message, 'name': users.username})
def aboutus(request):
      return render(request,'aboutus.html')

def emp_home(request):
      return render(request,'emp_home.html')
def newrequest(request):
      if request.method=='POST':
            name=request.POST.get('product')
            company=request.POST.get('brand')
            model=request.POST.get('model')
            address=request.POST.get('address')
            user=auth.get_user(request)
            products=product.objects.create(name=name, company=company,model=model,customer=user)
            obj = employee.objects.all().order_by('work')[0]
            obj.work += 1
            print(obj.work)
            obj.save()
            products.save()
            ser = service.objects.create(customer=user, address=address, employee=obj,
                                         date=datetime.date.today() + datetime.timedelta(days=2))
            ser.save()
            return redirect(myaccount)
def cancel(request):
      user=auth.get_user(request)
      ser=service.objects.filter(customer_id=user.id).all()
      ser.delete()
      pro=product.objects.filter(customer_id=user.id).all()
      pro.delete()
      return redirect(myaccount)

