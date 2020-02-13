"""mysite URL Configuration

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls import include, url
import Student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson4', include('lesson4.urls')),
    path('teacher/', include('Teacher.urls')),
    path('group/', include('Group.urls')),
    path('student/', include('Student.urls')),
    path('', include('Group.urls'), name='base'),
]

handler404 = Student.views.handler404
handler500 = Student.views.handler500


if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
