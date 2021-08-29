from django.urls import path
from . import views

app_name = 'myPage'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
]
