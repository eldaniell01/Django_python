from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
app_name='chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_user, name='logout')
]
