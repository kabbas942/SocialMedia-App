from django.shortcuts import render,HttpResponse,redirect
from accounts.models import Profile
from accounts.modelForm import profileForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.


class profileListView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'accounts/index.html'

def userLogin(request):
    if request.method=="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/profile')
        else:
            return render(request, 'accounts/userLogin.html', {'error_message': 'Invalid username or password.'})
    return render(request,'accounts/userLogin.html')


@login_required
def forgotPassword(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"accounts/forgotPassword.html")


def createAccount(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"accounts/userLogin.html")


@login_required
def profileMainPage(request):
    profileData = Profile.objects.get(user=request.user)
    form =profileForm(request.POST or None, request.FILES or None, instance=profileData)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    context={'profileData':profileData,'profileForm':form}
    return render(request,"accounts/profile.html",context)