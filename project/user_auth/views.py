from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from social_django.models import UserSocialAuth

@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    pageDic = {
    'user': user
}
    print(user.extra_data)
    return render(request,'user_auth/top.html',pageDic)

