from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    # social login views on custom signup page
    # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       username = form.cleaned_data.get('username')
#       messages.success(request, f"New account created: {username}")
#       login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#     else:
#       messages.error(request,"Account creation failed")

#     return redirect("main:homepage")

#   form = UserCreationForm()
#   return render(request,"register.html", {"form": form})
