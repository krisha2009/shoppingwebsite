from django.shortcuts import render
from login.models import User

# Create your views here.
def home(request):
        return render(request,'homepage.html')

def createacc(request):
        if request.method == 'POST':
                email=request.POST['email']
                contact=request.POST['contact']
                uname=request.POST['uname']
                password=request.POST['password']
                #print(email,contact,uname,password)
                ins=User(email=email,contact=contact,uname=uname,password=password)
                ins.save()
            
               
        return render(request, 'createacc1.html')  

        
def login(request):
        return render(request,'login.html')

def login1(request):
        return render(request,'login1.html')