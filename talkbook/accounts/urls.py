from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.userLogin,name="userLogin"),
    path('forgotPassword',views.forgotPassword,name="forgotPassword")
]