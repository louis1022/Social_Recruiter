
from django.contrib import admin
from django.urls import path

from manager import views
import manager.views as manager_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker_list/', manager_view.WorkerListView.as_view()),  # URLとViewを組み合わせる！
    path('', manager_view.home.as_view()),
]

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url('__debug__/', include(debug_toolbar.urls)),
    ]
