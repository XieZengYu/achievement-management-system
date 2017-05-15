"""achievement_management_system URL Configuration

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
from django.contrib import admin
from admin_operation.views import *
from user_management.views import *
from teacher_operation.views import *
from student_operation.views import *
from CourseAndScore.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login,name="login"),
    url(r'^index/', index,name="index"),
    url(r'^news/(\d+)/$', news,name="news"),
    url(r'^update/(?P<pk>\d+)/', PersonUpdate.as_view(),name="update"),
    url(r'^t_update/(?P<pk>\d+)/$', TeacherUpdate.as_view(),name="t_update"),
    url(r'^changepassword/', ChangePassword,name="changepwd"),
    url(r'^Course/', course,name="course"),
    url(r'^Score/', score,name="score"),
    url(r'^Analyze/', analyze,name="analyze"),
    url(r'^upload_c/', campusinfo,name="campusinfo"),
    url(r'^upload_1/', userimport,name="userimport"),
    url(r'^upload_2/', courseimport,name="courseimport"),
    url(r'^upload_3/', scoreimport,name="scoreimport"),
    url(r'^upload_t/', t_scoreimport,name="t_scoreimport"),
    url(r'^Search_s/', search_s,name="search_s"),
    url(r'^Search_t/', search_t,name="search_t"),
]
