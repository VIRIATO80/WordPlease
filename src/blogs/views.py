from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime

from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView

from blogs.forms import SignUpForm, PostForm

from blogs.models import Post


def home(request):
    now = datetime.now()
    all_post = Post.objects.filter(publish_date__lte=now).order_by("-publish_date")
    context = {'posts': all_post}
    return render(request, "home.html", context)


def user_posts_list(request, nombre_usuario):
    now = datetime.now()
    posts_list = Post.objects.filter(user__username=nombre_usuario, publish_date__lte=now).order_by("-publish_date")
    context = {'posts': posts_list, 'owner': nombre_usuario}
    return render(request, "my_blog.html", context)


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
    template_name = 'post_detail.html'


    def get_queryset(self):
        query = super(PostDetailView, self).get_queryset()
        now = datetime.now()
        return query.filter(publish_date__lte=now)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return render(request,"404.html")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)