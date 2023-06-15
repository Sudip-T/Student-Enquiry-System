from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_student'),
    path('create/', create, name='create_student'),
    path('edit/<int:pk>/', edit, name='edit_student'),
    path('display/<int:pk>/', show, name='show_student'),
    path('delete/<int:pk>/', delete, name='delete_student'),
]