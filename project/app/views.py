from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView, View

APP_NAME = 'app'

class TopPage(TemplateView):
    template_name = '%s/index.html' % APP_NAME

class DashboardPage(TemplateView):
    template_name = '%s/dashboard.html' % APP_NAME
