from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.layout, name='layout'),
    # path('base/',  Template.as_view(), name='base'),

]