from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('listview', views.ListSpices.as_view(), name='listview'),
    path('addspice/', views.AddSpice.as_view(), name='addspice'),
    ]
