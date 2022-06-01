from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name= 'index'),
    path('specific/<str:pk>',views.specific, name= 'specific'),
]