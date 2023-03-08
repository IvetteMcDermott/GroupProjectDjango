from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('listview', views.ListSpices.as_view(), name='listview'),
    path('<slug:slug>/', views.SpiceDetail.as_view(), name='spice_detail'),
    path('addspice/', views.AddSpice.as_view(), name='addspice'),
    ]
