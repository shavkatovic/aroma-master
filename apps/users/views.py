# Create your views here.
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import RegisterForm, CustomLoginForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    model = User

    def form_valid(self, form):
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('register')

    def form_invalid(self, form):
        return redirect('login')
