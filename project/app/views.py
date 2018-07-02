from django.views.generic.base import View
from django.shortcuts import render

APP_NAME = 'app'

class TopPage(View):
    template_name = '%s/index.html' % APP_NAME
    def get(self, request):
        return render(request, self.template_name)
