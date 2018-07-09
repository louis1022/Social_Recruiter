from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic,View
from django.views.generic import CreateView, UpdateView
from .models import Message
from .forms import MessageForm

APP_NAME = 'app'

class TopPage(generic.TemplateView):
    template_name = '%s/index.html' % APP_NAME

class CreateMessage(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "app/form.html"
    success_url = "/"
