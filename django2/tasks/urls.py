from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^tasks/$', views.CourseList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
]