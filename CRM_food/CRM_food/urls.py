"""CRM_food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from CRM import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^department/$', views.DepartmentList.as_view()),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
    url(r'^meal/$', views.MealList.as_view()),
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),
    url(r'^check/$', views.CheckList.as_view()),
    url(r'^check/(?P<pk>[0-9]+)/$', views.CheckDetail.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^status/$', views.StatusList.as_view()),
    url(r'^status/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view()),
    url(r'^role/$', views.RoleList.as_view()),
    url(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view()),
]
