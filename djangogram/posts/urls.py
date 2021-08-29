from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('myPage/', views.my_page, name='my_page'),
    path('edit/', views.edit, name='edit'),
]
