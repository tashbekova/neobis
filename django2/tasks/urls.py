from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from tasks import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    url(r'^tasks/$', views.CourseList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
]