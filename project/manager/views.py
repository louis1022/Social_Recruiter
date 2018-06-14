from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *


class home(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all().select_related('person')  # 変更部分
        context['workers'] = workers # html内でworkersという変数を有効にする。

        return render(self.request, self.template_name, context)
