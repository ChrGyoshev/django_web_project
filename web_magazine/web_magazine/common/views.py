from django.shortcuts import render
from django.views import generic as views
# Create your views here.
class Index(views.TemplateView):
    template_name = 'index.html'


class ErrorPage(views.TemplateView):
    template_name =  '404.html'