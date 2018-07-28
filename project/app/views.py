from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView
from social_django.models import UserSocialAuth

from app.models import Person
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse_lazy
from django.views import generic,View
from django.contrib import messages
from .models import Introduce,Message
from .forms import IntroduceForm,MessageForm,ContactForm


APP_NAME = 'app'


class DashboardPage(TemplateView):
    template_name = '%s/dashboard.html' % APP_NAME

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            self.template_name = '%s/lp.html' % APP_NAME
            return render(request, self.template_name, {})
        elif request.user.is_authenticated:
            user = UserSocialAuth.objects.get(user_id=request.user.id)
            return render(request, self.template_name, {'user': user})


class userProfilePage(LoginRequiredMixin, TemplateView):
    template_name = '%s/user.html' % APP_NAME

    def get(self, request, *args, **kwargs):
        user = UserSocialAuth.objects.get(user_id=request.user.id)
        return render(request, self.template_name, {'user': user})



class tablesPage(LoginRequiredMixin, ListView):
    template_name = '%s/tables.html' % APP_NAME
    model = Person
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            q = q.strip().split(' ')
            person = Person.objects.filter()
            for i in q:
                person=person.filter(description__icontains=i)
            return person

        else:
            return Person.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['count'] = self.get_queryset().count()
        context['page'] = self.request.GET.get('page')

        return context

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

class ContactView(FormView):
    template_name = "app/contactForm.html"
    form_class = ContactForm
    success_url = "/contact"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
