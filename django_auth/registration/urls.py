from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), 
    name='profile'),
]
