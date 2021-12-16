from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('artical/<int:pk>', views.PostDetailView.as_view(), name='post_detail_view'),
    path('crate_post/', views.AddPostView.as_view(), name='create_post'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
