
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # Home page
    path('about/', views.about, name='about'), # About page
    path('projects/', views.projects, name='projects'), # Projects page
]
