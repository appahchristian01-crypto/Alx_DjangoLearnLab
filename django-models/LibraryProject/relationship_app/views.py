from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm  # This is the built-in Django signup form
    success_url = reverse_lazy("login")  # After signing up, go to login page
    template_name = "registration/signup.html"  # Which template to use
