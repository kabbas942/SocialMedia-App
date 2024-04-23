from django.shortcuts import render,HttpResponse
from accounts.models import Profile
from accounts.modelForm import profileForm

# Create your views here.
def userLogin(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"accounts/userLogin.html")

def forgotPassword(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"accounts/forgotPassword.html")

def createAccount(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"accounts/userLogin.html")

def profileMainPage(request):
    profileData = Profile.objects.get(user=request.user)
    context={'profileData':profileData,'profileForm':profileForm()}
    return render(request,"accounts/profile.html",context)