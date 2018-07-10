from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic,View
from django.contrib import messages
from django.shortcuts import get_object_or_404,render,redirect
from social_django.models import UserSocialAuth
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

APP_NAME = 'app'

class TopPage(generic.TemplateView):
    template_name = '%s/index.html' % APP_NAME

# class CreateMessage(CreateView):
#     # model = Message
#     form_class = MessageForm
#     template_name = "app/form.html"
#     success_url = "/create"
#     def form_valid(self, form):
#         test = Message(message=form.cleaned_data['message'])
#         user = get_object_or_404(UserSocialAuth, user_id=self.request.user.id)
#         test.user = user
#         test.save()
#         messages.success(self.request, "保存しました")
#         return super().form_valid(form)

# Modelformmixin

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

    success_url = reverse_lazy(get_message)

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))

        return result
