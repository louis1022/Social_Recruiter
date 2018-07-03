from django.shortcuts import render

from django.views.generic.base import View
from django.views.generic import TemplateView

APP_NAME = 'app'

class TopPage(TemplateView):
    template_name = '%s/index.html' % APP_NAME
