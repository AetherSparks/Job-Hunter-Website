from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import ProfileForm, UserUpdateForm
from .forms import ProfileForm, UserUpdateForm
from .forms import UserUpdateForm, ProfileUpdateForm, ProfileForm, UserRegisterForm, UserLoginForm


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'myapp/edit_profile.html', context)






def home(request):
    return render(request, 'myapp/home.html')


def add_job(request):
    return render(request, 'myapp/add_job.html')


def employer_dashboard(request):
    return render(request, 'myapp/employer_dashboard.html')


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user  
    }
    return render(request, 'myapp/profile.html', context)




def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
           
            username = request.POST['loginEmail']
            password = request.POST['loginPassword']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  
            else:
                messages.error(request, 'Invalid username or password.')
                print("Login failed: Invalid username or password.")  

        elif 'register' in request.POST:
           
            name = request.POST['registerName']
            username = request.POST['registerEmail']
            password = request.POST['registerPassword']
            confirm_password = request.POST['registerConfirmPassword']
            user_type = request.POST['registerUserType']

            if password == confirm_password:
                try:
                   
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'Email address already registered.')
                        print("Registration failed: Email address already registered.") 
                    else:
                        
                        user = User.objects.create_user(username=username, password=password)
                        user.first_name = name
                        user.save()
                        login(request, user)
                        return redirect('profile')  # Redirect to profile page after registration
                except Exception as e:
                    messages.error(request, f'Error creating user: {e}')
                    print(f"Registration failed: {e}")  # Debug statement
            else:
                messages.error(request, 'Passwords do not match.')
                print("Registration failed: Passwords do not match.")  # Debug statement

    return render(request, 'myapp/login_register.html')


def find_jobs(request):
    return render(request, 'myapp/find_jobs.html')
