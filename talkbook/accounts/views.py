from django.shortcuts import render,HttpResponse
from accounts.models import Profile
from accounts.modelForm import profileForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class profileListView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'accounts/index.html'

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
    form =profileForm(request.POST or None, request.FILES or None, instance=profileData)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            


    context={'profileData':profileData,'profileForm':form}
    return render(request,"accounts/profile.html",context)