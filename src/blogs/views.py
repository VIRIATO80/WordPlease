from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from blogs.forms import SignUpForm, PostForm

from blogs.models import Post


def home(request):
    all_post = Post.objects.all().order_by("-publish_date")
    context = {'posts': all_post}
    return render(request, "home.html", context)

def user_posts_list(request, nombre_usuario):
    posts_list = Post.objects.filter(user__username=nombre_usuario).order_by("-publish_date")
    # posts_list = Post.objects.get(user.username=nombre_usuario).order_by("-publish_date")
    context = {'posts': posts_list}
    return render(request, "home.html", context)

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
            #  Autenticamos directamente al nuevo usuario
            login(request, user)
            return redirect("home_page")
        return render(request, "signup.html", {"form": form})


class CreatePostView(View):

    def get(self, request):
        form = PostForm()
        return render(request, "create_post_form.html", {"form": form})

    def post(self, request):
        post = Post()
        post.user = request.user  # Asignamos el usuario autenticado
        form = PostForm(request.POST,  request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("home_page")
        return render(request, "create_post_form.html", {"form": form})

