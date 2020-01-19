from django.urls import path
from Student.views import student, student_add, student_edit

urlpatterns = [
    path('', student, name='student'),
    path('add/', student_add, name='student-add'),
    path('edit/<int:pk>/', student_edit, name='student-edit'),
]
