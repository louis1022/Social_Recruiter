from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic,View
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.shortcuts import get_object_or_404,render,redirect
from social_django.models import UserSocialAuth
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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            test = Message(message=form.cleaned_data['message'])
            user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
            test.user = user
            test.save()
            messages.success(request, "保存しました")
            return redirect('/create')
    else:
        form = MessageForm()

    return render(request, 'app/form.html', {'form':form})
