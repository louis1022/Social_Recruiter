from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from social_django.models import UserSocialAuth

APP_NAME = 'app'


class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = '%s/dashboard.html' % APP_NAME

    def get(self, request, *args, **kwargs):
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
        user = UserSocialAuth.objects.get(user_id=request.user.id)
        return render(request, self.template_name, {'user': user})
