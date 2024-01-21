from django.shortcuts import render,HttpResponse

# Create your views here.
def userLogin(request):
    return render(request,"accounts/userLogin.html")

def forgotPassword(request):
    return render(request,"accounts/forgotPassword.html")