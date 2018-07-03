from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

app_name = 'accounts'
top_app_name = 'app'

@login_required
def top_page(request):
    template_name = '%s/index.html' % top_app_name

    user = UserSocialAuth.objects.get(user_id=request.user.id)
    return render(request, template_name, {'user': user})
