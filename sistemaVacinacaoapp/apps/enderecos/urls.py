from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'enderecos'

router = routers.DefaultRouter()
router.register('', views.EnderecosViewSet, basename='enderecos')

urlpatterns = [
    path('', include(router.urls) )
]