from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.views.generic import TemplateView, View
from social_django.models import UserSocialAuth

from app.models import Person
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.views import generic,View
from django.contrib import messages
from .models import Introduce
from .forms import IntroduceForm

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

def get_message(request):
    user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
    mess = Message.objects.filter(user=user)
    if request.method == 'POST':
        form = MessageForm(request.POST) # request.POSTに送られてきたデータがある
        if form.is_valid():
            post = form.save(commit=False) # まだMessageモデルは保存しない
            user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
            post.user = user
            post.save()
            messages.success(request, "保存しました")
            return redirect('/message/create')
    else: # 初回アクセスで空のformほしい
        form = MessageForm()

    return render(request, 'app/form.html', {'form':form, 'mess':mess})

class UpdateMessage(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "app/form_update.html"
    success_url = "/message/create"

class DeleteMessage(generic.DeleteView):
    model = Message
    form_class = MessageForm

    success_url = reverse_lazy('app:create')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))

        return result

def user_page(request):
    user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
    #mess = Introduce.objects.get(user=user)
    if request.method == 'POST':
        form = IntroduceForm(request.POST) # request.POSTに送られてきたデータがある
        print(form)
        if form.is_valid():
            if not Introduce.objects.filter(user=user).exists():
                post = form.save(commit=False) # まだIntroduceモデルは保存しない
                user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
                post.user = user
                post.save()
                messages.success(request, "保存しました")
                return redirect('/user')
            else:
                intro = get_object_or_404(Introduce, user_id=request.user.id)
                form = IntroduceForm(request.POST, instance=intro)
                form.save()
                return redirect('/user')
    else: # 初回アクセスで空のformほしい
        if not Introduce.objects.filter(user=user).exists():
            form = IntroduceForm()
        else:
            intro = get_object_or_404(Introduce, user_id=request.user.id)
            form = IntroduceForm(instance=intro)


    return render(request, 'accounts/top.html', {'form':form, 'user':user})
