from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from blogs.forms import SignUpForm
from blogs.models import BlogPersonal


def home(request):
    return render(request, "home.html")


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Grabamos el usuario desde el formulario
            user = form.save()
            user.save()
            blog = BlogPersonal()
            blog.user = user  # Asignamos el usuario recien creado
            #  Grabamos el blog en la plataforma
            blog.save()
            #  Autenticamos directamente al nuevo usuario
            login(request, user)
            return render(request, "home.html")
        return render(request, "signup.html", {"form": form})
