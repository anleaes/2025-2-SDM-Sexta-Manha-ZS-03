from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'fabricante'

router = routers.DefaultRouter()
router.register('', views.FabricanteViewSet, basename='fabricante')

urlpatterns = [
    path('', include(router.urls) )
]