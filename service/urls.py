from django.urls import path

from . import views

urlpatterns = [
    path('service/', views.service, name='service'),
    path('service-details/', views.service_details, name='service-details'),

]
