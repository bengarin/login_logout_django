from django.shortcuts import render , redirect
from formsJson.forms import  CustomizeFormUser
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login as auth_login 
def sing_up(request):
    if request.user.is_authenticated:
        return redirect('home') 
    form = CustomizeFormUser()
    if request.method == 'POST':
        form = CustomizeFormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect("login")
        else :
            form = CustomizeFormUser(request.POST)
    else :
        form = CustomizeFormUser()        
    context = {
        'form': form,
    }
    return render(request, 'user/signup.html',context)




def login(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login  (request,user)
            return redirect('home')
        else : 
            messages.add_message(request, messages.ERROR, 'Invalid username or password!', extra_tags='danger')
    context = {}
    return render(request, 'user/login.html',context)


def logout_user(request):
    logout(request)
    return redirect('login')