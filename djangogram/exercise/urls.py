from django.urls import path
from . import views

app_name = 'exercise' # app_name
# url 매핑
urlpatterns = [
    path('', views.start, name='start'),
    path('playlist/', views.playlist, name='playlist'),
    path('routine/', views.routine, name='routine'),
]
# path의 첫번째 인자는 주소 매핑, 두번째 인자는 호출할 함수
