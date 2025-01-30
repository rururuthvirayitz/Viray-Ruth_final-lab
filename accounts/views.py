from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm  # Import the custom form

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use custom form
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Redirect after successful signup
