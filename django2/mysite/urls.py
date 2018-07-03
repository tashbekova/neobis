from django.conf.urls import  url,include
from django.contrib.auth.models import User
from django.contrib import admin

urlpatterns = [
    url(r'^', include('tasks.urls')),
    url(r'^drf/', include('snippets.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include('web.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
