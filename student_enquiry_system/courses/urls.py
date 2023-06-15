from django.urls import path
from .views import * 


urlpatterns = [
    path('', index, name='index_course'),
    path('create/', create, name='create_course'),
    path('edit/<int:pk>/', edit, name='edit_course'),
    # path('display/<int:pk>/', show, name='show_course'),
    path('delete/<int:pk>/', delete, name='delete_course'),
]