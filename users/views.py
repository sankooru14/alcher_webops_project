from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect ('login')
        
            
    return render(request, 'users/register.html', {'form':form})
    


    
