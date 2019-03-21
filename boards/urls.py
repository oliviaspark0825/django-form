from django.urls import path
from . import views

app_name = 'boards'

urlpatterns= [
    #views에 있는 create 함수를 받겠다 name == create html 을 저거로 받겠다
    path('<int:board_pk>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('', views.index, name='index'),
    ]