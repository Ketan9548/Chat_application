from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('<str:room>/',room,name="room"),
    path('checkview',checkview,name="checkview"),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]