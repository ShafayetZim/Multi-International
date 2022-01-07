from django.urls import path
from . import views

urlpatterns = [
    # Menu
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # Dashboard
    # Home
    path('dashboard/feature', views.FeatureView.as_view(), name='feature'),  # Feature
    path('dashboard/feature-edit/<int:pk>', views.FeatureUpdateView.as_view(), name='feature-edit'),  # Feature edit
    path('dashboard/feature-create', views.create_feature, name='create-feature'),  # create feature
    path('dashboard/feature-delete/<int:id>', views.delete_feature, name='delete-feature'),  # delete slider
    # Slider
    path('dashboard/slider', views.SliderView.as_view(), name='slider'),  # slider
    path('dashboard/slider-edit/<int:pk>', views.SliderUpdateView.as_view(), name='slider-edit'),  # slider edit
    path('dashboard/slider-create', views.create_slider, name='create-slider'),  # create slider
    path('dashboard/slider-delete/<int:id>', views.delete_slider, name='delete-slider'),  # delete slider
    # Process
    path('dashboard/process', views.WorkingProcessView.as_view(), name='process'),  # Process
    path('dashboard/process-edit/<int:pk>', views.WorkingProcessUpdateView.as_view(), name='process-edit'),  # Process edit
    path('dashboard/process-create', views.create_process, name='create-process'),  # create process
    path('dashboard/process-delete/<int:id>', views.delete_process, name='delete-process'),  # delete process
    # About
    path('dashboard/about', views.AboutView.as_view(), name='dash-about'),  # About
    path('dashboard/about-edit/<int:pk>', views.AboutUpdateView.as_view(), name='about-edit'),  # About edit
    # Choice
    path('dashboard/choice', views.ChoiceView.as_view(), name='choice'),  # Choice
    path('dashboard/choice-edit/<int:pk>', views.ChoiceUpdateView.as_view(), name='choice-edit'),  # Choice edit
    path('dashboard/choice-create', views.create_choice, name='create-choice'),  # create choice
    path('dashboard/delete-choice/<int:id>', views.delete_choice, name='delete-choice'),  # delete choice
    # Team
    path('dashboard/team', views.TeamView.as_view(), name='team'),  # Team
    path('dashboard/team-create', views.create_team, name='create-team'),  # create team
    path('dashboard/team-edit/<int:pk>', views.TeamUpdateView.as_view(), name='team-edit'),  # Team edit
    path('dashboard/delete-team/<int:id>', views.delete_team, name='delete-team'),  # delete team
    # Vision
    path('dashboard/vision', views.VisionView.as_view(), name='vision'),  # Vision
    path('dashboard/vision-edit/<int:pk>', views.VisionUpdateView.as_view(), name='vision-edit'),  # Vision edit
    path('dashboard/vision-create', views.create_vision, name='create-vision'),  # create vision
    path('dashboard/delete-vision/<int:id>', views.delete_vision, name='delete-vision'),  # delete vision
    # Contact
    path('dashboard/contact', views.ContactView.as_view(), name='dash-contact'),  # Contact
    path('dashboard/contact-edit/<int:pk>', views.ContactUpdateView.as_view(), name='contact-edit'),  # Contact edit
    # Gallery
    path('dashboard/gallery', views.GalleryView.as_view(), name='dash-gallery'),  # Gallery
    path('dashboard/gallery-edit/<int:pk>', views.GalleryUpdateView.as_view(), name='gallery-edit'),  # Gallery edit
    path('dashboard/gallery-create', views.create_gallery, name='gallery-create'),  # Gallery create
    path('dashboard/delete-gallery/<int:id>', views.delete_gallery, name='delete-gallery'),  # Gallery delete
    # Service
    path('dashboard/service', views.ServiceView.as_view(), name='dash-service'),  # Service
    path('dashboard/service-edit/<int:pk>', views.ServiceUpdateView.as_view(), name='service-edit'),  # Service edit
    path('dashboard/service-create', views.create_service, name='create-service'),  # create service
    path('dashboard/delete-service/<int:id>', views.delete_service, name='delete-service'),  # delete service

]
