from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/sign.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quote:root")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print("form")
        print(form)
        if form.is_valid():
            print(f"Аккаунт для створено")
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Аккаунт для {username} створено')
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})


