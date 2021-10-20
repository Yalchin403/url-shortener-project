from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CreateUserForm


class SignUp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('backend:generate-url')
        else:
            form = CreateUserForm()
            context = {'form': form}
            return render(request, "accounts/signup.html", context)
    def post(self, request):

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            user_obj = User.objects.get(username=user)
            user_obj.save()
            messages.success(request, f'{user}, account has been successfully created for you')
            return redirect('accounts:signIn')
        else:
            return render(request, 'accounts/signup.html', {'form':form})

class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('backend:generate-url')
        return render(request, 'accounts/signin.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:generate-url')
            
        else:
            messages.info(request, 'Username or password invalid')
            return render(request, 'accounts/signin.html')

        messages.error(request, "Your account is not active!")
        return render(request, 'accounts/signin.html')


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:signIn')