from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("login/",views.loginProccess,name="loginProcess"),
    path("logout/",views.logoutProccess,name="logoutProccess"),
    path("signup/",views.signup,name="signup"),
    path("profile/",views.profile,name="profile"),
    path("works/",views.works,name="works"),
    path("contact/",views.contact,name="contact"),
    path("news/",views.news,name="news"),
    path("state/<str:state>/",views.FillupForm,name="state"),

]
