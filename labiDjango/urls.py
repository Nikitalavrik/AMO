"""labiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from menu.views import homepage
from lab1.views import laboratory1,part1,part2,part3

urlpatterns = [
    url(r'^$',homepage, name="homepage"),
    url(r'^lab1/',laboratory1, name="lab1"),
    url(r'^lab1_part1/',part1, name="lab1_part1"),
    url(r'^lab1_part2/',part2, name="lab1_part2"),
    url(r'^lab1_part3/',part3, name="lab1_part3"),
    url(r'^admin/', admin.site.urls),
]
