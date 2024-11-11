from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def landing(request):
    return render(request, 'landing/landing.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect(reverse_lazy("landing:logIn"))  # Redirect to login page after registration
        else:
            messages.success(request, "Comprueba los datos de la cuenta")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'landing/signIn.html', {'form': form})


class LoginUserView(FormView):
    form_class = AuthenticationForm
    template_name = "landing/logIn.html"
    success_url = reverse_lazy("POS:homePOS")
    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        contra = form.cleaned_data.get('password')
        user = authenticate(self.request, username=usuario, password=contra)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Handle the case where authentication fails
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)
        
def logOutUser(request):
    logout(request)  # Logs out the current user
    return redirect(reverse_lazy("landing:landing"))

