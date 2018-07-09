from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from social_django.models import UserSocialAuth

from app.models import Person

APP_NAME = 'app'



class DashboardPage(TemplateView):
    template_name = '%s/dashboard.html' % APP_NAME

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            self.template_name = '%s/top.html' % APP_NAME
            return render(request, self.template_name, {})
        elif request.user.is_authenticated:
            user = UserSocialAuth.objects.get(user_id=request.user.id)
            return render(request, self.template_name, {'user': user})


class userProfilePage(LoginRequiredMixin, TemplateView):
    template_name = '%s/user.html' % APP_NAME

    def get(self, request, *args, **kwargs):
        user = UserSocialAuth.objects.get(user_id=request.user.id)
        return render(request, self.template_name, {'user': user})


class tablesPage(LoginRequiredMixin, TemplateView):
    template_name = '%s/tables.html' % APP_NAME

    def get(self, request, *args, **kwargs):
        context = super(tablesPage, self).get_context_data(**kwargs)
        persons = Person.objects.all()
        context['persons'] = persons
        return render(request, self.template_name, context)
