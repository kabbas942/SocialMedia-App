from django.shortcuts import render,HttpResponse

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