from django.contrib import admin
from django.urls import path, include
from tasks import views as tasks_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include('tasks.urls')),
    path("", tasks_views.home_view)
]

urlpatterns += staticfiles_urlpatterns()
