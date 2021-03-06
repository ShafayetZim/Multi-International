"""multi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.conf import settings
from users import views as user_views
from django.conf.urls.static import static

admin.site.site_header = "Multi International"
admin.site.site_title = "Welcome to Admin Site"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
    # path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('user-register/', user_views.register, name='user-register'),
    path('profile/', user_views.profile, name='profile'),
    path('user-login/', auth_views.LoginView.as_view(template_name='user-login.html'), name='user-login'),
    path('user-logout/', auth_views.LogoutView.as_view(template_name='user-logout.html'), name='user-logout'),
    # path('admin-mi/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('service.urls')),
    path('', include('gallery.urls')),
    path('', include('contact.urls')),
    path('', include('dashboard.urls')),
    # path('tinymce/', include('tinymce.urls')),
    # path('accounts/',include('django.contrib.authentication.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
