


from django.urls import path
from .views import Register_view,User_logout_View,User_Login_View,dash
urlpatterns = [
    path("",Register_view,name="user registration"),
    path("logout/", User_logout_View.as_view(), name="user logout"),
    path("login/", User_Login_View, name="user login"),
    path("dash/", dash, name="dash"),
    
]
















