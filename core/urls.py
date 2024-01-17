from django.urls import path
from core import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.auth import views as auth_views 
from .forms import LoginForm 
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'), 
     path("logout/", views.logout_view, name= "logout_view"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)