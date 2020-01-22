"""api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path, path
from rest_framework import routers
from rest_framework.authtoken import views as rsf_auth_views
from novelty import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'novelties', views.NoveltyViewSet)
router.register(r'nodes', views.NodeViewSet)
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # patterns
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api-token-auth/', rsf_auth_views.obtain_auth_token),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    path('notificaciones/', views.Notificaciones.as_view()),

]

urlpatterns += router.urls