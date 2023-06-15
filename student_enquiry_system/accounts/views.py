import re
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class DashboardView(LoginRequiredMixin, View):
    login_url = 'members/login' 

    def get(self, request):
        return render(request, 'layouts/dashboard.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')  # Get the value of the 'next' parameter
            messages.success(request, 'Login successfull!')
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' URL
            else:
                return redirect('dashboard')
            return redirect('dashboard')
        messages.error(request, 'Login failed! Check username or password...')
        return redirect('log_in')
    

class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

         # Check if the email already exists in the database
    #     if self.is_duplicate(username, email):
    #         messages.error(request, 'Email already taken. Try chaging email or proceed to login')
    #         return redirect('register')
        
    # def is_duplicate(self, username, email):
    #     if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
    #         return True
    #     return False
        
        # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        
        # Check if the email already exists in the database
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken. Try chaging email or proceed to login')
            return redirect('register')

        # Password validation
        if len(password) < 8 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.error(request, 'Password must be at least 8 characters long and contain a special character.')
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            if user is not None:
                user.is_active=True
                user.save()
                # Authenticate and log in the user
                authenticated_user = authenticate(request, username=username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    messages.success(request, 'Account registration successful!')
                    return redirect('dashboard')
            messages.error('Something went wrong! Plese make sure email and password input are correct.')
            return redirect('register')
        except:
            messages.error(request, 'Something went wrong.')
            return redirect('register')
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('log_in')
    

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)