from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUsers

# def home(request):
#     return render(request, 'user_app/post_list.html')
from user_app.models import Post


class PostView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'user_app/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'user_app/create_post.html'
    # fields = '__all__'


class UserRegisterView(CreateView):
    form_class = CreateUsers
    template_name = 'user_app/register.html'
    success_url = reverse_lazy('login')

