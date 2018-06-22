from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include('web.urls')),
    url(r'^polls/', include('polls.urls')),
]
