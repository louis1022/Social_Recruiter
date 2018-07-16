from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.shortcuts import get_object_or_404,render,redirect
from .models import Introduce
from .forms import IntroduceForm
from django.contrib import messages
from django.views import generic

app_name = 'accounts'

# @login_required
# def top_page(request):
#     template_name = '%s/top.html' % app_name
#
#     user = UserSocialAuth.objects.get(user_id=request.user.id)
#     return render(request, template_name, {'user': user})

@login_required
def user_page(request):
    user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
    mess = get_object_or_404(Introduce, user=user)
    print(type(mess))
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
                user = get_object_or_404(Introduce, user_id=request.user.id)
                post = IntroduceForm(request.POST, instance=user)
                post.save()
                return redirect('/user')
    else: # 初回アクセスで空のformほしい
        form = IntroduceForm()

    return render(request, 'accounts/top.html', {'form':form, 'user':user, 'mess':mess})
