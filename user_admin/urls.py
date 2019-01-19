"""runconde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

# app_name = 'user_admin'     # 可以 <a href="{% url 'user_admin:index' %}">，以区别不同app下的同一个命空间
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^useradmin/$', views.useradmin_base, name='useradmin'),
    url(r'^useradmin/change_password', views.useradmin_change_password, name='useradmin_change_password'),
    url(r'^useradmin/change_email', views.useradmin_change_email, name='useradmin_change_email'),
    url(r'^ajax_check_username/', views.ajax_check_username, name='ajax_check-username'),
    url(r'^ajax_check_old_email/', views.ajax_check_old_email, name='ajax_check_old_email'),
    url(r'^ajax_send_yzm/', views.ajax_send_yzm, name='ajax_send_yzm'),
]
