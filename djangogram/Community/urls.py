from django.urls import path
from . import views

app_name = 'Community' # app_name
# url 매핑
urlpatterns = [
    path('', views.feed, name='feed'),
    path('edit/', views.edit, name='edit'),
    # path('feed/', views.feed, name='feed'),
    path('create/', views.create, name='create'),
]
# path의 첫번째 인자는 주소 매핑, 두번째 인자는 호출할 함수
