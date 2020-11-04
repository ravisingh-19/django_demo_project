from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'
