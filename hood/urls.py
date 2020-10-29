from django.urls import path,re-path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
]
