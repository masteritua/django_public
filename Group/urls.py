from django.urls import path
from Group.views import group, group_add, group_edit

urlpatterns = [
    path('', group, name='group'),
    path('add/', group_add, name='group-add'),
    path('edit/<int:pk>/', group_edit, name='group-edit'),
]
