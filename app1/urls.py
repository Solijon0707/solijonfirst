from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('todo/',index,name='index'),
    path('edit/<int:id>/',edit1,name='edit'),
    path('delete/<int:id>/',delete1,name='delete'),
    path('add/',ad,name='ad'),
    path('translate/',translat,name='translat'),

]