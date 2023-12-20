from django.urls import path
from . import views

app_name='room'
urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.detail_room, name='roo')
]
