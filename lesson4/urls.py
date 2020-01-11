from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_student, name='generate_student'),
]
