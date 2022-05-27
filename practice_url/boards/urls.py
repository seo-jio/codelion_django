from django.urls import path
from boards import views

urlpatterns = [
    path('', views.board),
    path('first/', views.boardfirst),
]