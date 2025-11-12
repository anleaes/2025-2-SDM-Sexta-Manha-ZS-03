from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cidadao'

router = routers.DefaultRouter()
router.register('', views.CidadaoViewSet, basename='cidadao')

urlpatterns = [
    path('', include(router.urls) )
    ]