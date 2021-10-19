from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = "signUp"),
    path('login/', views.SignIn.as_view(), name = "signIn"),
    path('signout', views.SignOut.as_view(), name = "signOut"),
]