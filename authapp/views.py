from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method=='POST':
        
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!= password2:
            return HttpResponse('Your password and confirm password are not same')
        

        my_user= User.objects.create_user(email,password1)
        my_user.save()
        return redirect('/auth/login/')
    return render(request, 'signUp.html')

def handlelogin(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request,user)
        return redirect('/')
    return render(request, 'login.html')
    


    
def handlelogout(request):
    logout(request)
    return redirect('/auth/login/')
    return render(request,'logout.html')
     

