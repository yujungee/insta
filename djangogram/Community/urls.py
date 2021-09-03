from django.urls import path
from . import views

app_name = 'Community'
# url 매핑
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('feed/', views.feed, name='feed'),
]
