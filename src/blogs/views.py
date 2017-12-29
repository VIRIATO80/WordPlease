from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView

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


def blogs_list(request):
    all_blogs = User.objects.all().order_by("username")
    return render(request, "blogs_list.html", {"blogs": all_blogs})


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


class CreatePostView(LoginRequiredMixin, View):

    login_url = "/login"

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


class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def detail_view(request, pk):
        try:
            post_id = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404("Book does not exist")

        return render(request, 'post_detail.html', context={'post': post_id, })