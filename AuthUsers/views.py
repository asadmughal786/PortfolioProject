from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
#------------------------------- singup form buildin

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request,"user registered successfully!")
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

# ------------------------------Login Function buildin
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request,data = request.POST)
        if form.is_valid():
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            user  = authenticate(username = u_name,password= u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'User login Succeessfully!')
                return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

#-----------------------------------Profile function 

def user_profile(request):
    if request.user.is_authenticated:
        #-----------------User base login weather the user is Super or Normal-----------------
        if request.method=="POST":
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST,instance=request.user)
                users = None
            if form.is_valid():
                messages.success(request,'User Updated Successfully!')
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(instance = request.user)
                users = None
        return render(request,'profile.html',{'name':request.user,'form':form,'users':users})
    else:
        messages.error(request,'You are not authorized to access this page!')
        return HttpResponseRedirect('/login/')
# -------------------------------------Logout

def user_logout(request):
        logout(request)   
        messages.info(request,"Logout successfully!")
        return HttpResponseRedirect('/login/')
#--------------------Method 1 for changing the password by entering the Old pass as well-------------------
# def changepass(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = PasswordChangeForm(user=request.user , data = request.POST)
#             if form.is_valid():
#                 form.save()
#                 #This function is user to maintain the session for the user.
#                 update_session_auth_hash(request,form.user)
#                 messages.info(request,'Password Saved Successfully!')
#                 return HttpResponseRedirect('/profile/',)
#         else:
#             form = PasswordChangeForm(user=request.user)
#         return render(request,'changepass.html',{"form": form})
#     else:
#         messages.error(request,'You have no rights to access this page!')
#         return HttpResponseRedirect('/login/')


#-------------------------- method 2 Change Password without entering the old password----------------------------------------
def changepass1 (request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = SetPasswordForm(user= request.user,data=request.POST)
            if form.is_valid():
                form.save()
                #This function is user to maintain the session for the user.
                update_session_auth_hash(request,form.user)
                messages.info(request,'Password Saved Successfully!')
                return HttpResponseRedirect('/profile/',)
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{"form": form})
    else:
        messages.error(request,'You have no rights to access this page!')
        return HttpResponseRedirect('/login/')


def User_details(request, id):
    if request.user.is_authenticated:
        user_id = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance = user_id)
        return render(request, 'userdetails.html',{"form":form})
    else: 
        HttpResponseRedirect("/login/")