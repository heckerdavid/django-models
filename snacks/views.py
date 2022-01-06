from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from snacks.models import Snack

class HomePageView(TemplateView):
    template_name = 'home.html'

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack