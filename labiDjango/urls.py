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
from lab1.views import laboratory1, part1, part2, part3
from lab2.views import laboratory2, lab2_exec
from lab3.views import laboratory3, lab3_exec
from lab4.views import laboratory4, lab4_exec
from lab5.views import laboratory5, lab5_exec

urlpatterns = [
    url(r'^$', homepage, name="homepage"),
    url(r'^lab1/', laboratory1, name="lab1"),
    url(r'^lab2/', laboratory2, name="lab2"),
    url(r'^lab3/', laboratory3, name="lab3"),
    url(r'^lab4/', laboratory4, name="lab4"),
    url(r'^lab5/', laboratory5, name="lab5"),
    url(r'^lab2_exec/', lab2_exec, name="lab2_exec"),
    url(r'^lab3_exec/', lab3_exec, name="lab3_exec"),
    url(r'^lab4_exec/', lab4_exec, name="lab4_exec"),
    url(r'^lab5_exec/', lab5_exec, name="lab5_exec"),

    url(r'^lab1_part1/', part1, name="lab1_part1"),
    url(r'^lab1_part2/', part2, name="lab1_part2"),
    url(r'^lab1_part3/', part3, name="lab1_part3"),
    url(r'^admin/', admin.site.urls),
]
