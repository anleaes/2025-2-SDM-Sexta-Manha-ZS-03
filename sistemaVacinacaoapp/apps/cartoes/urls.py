from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cartoes'

router = routers.DefaultRouter()
router.register('', views.CartaoViewSet, basename='cartoes')

urlpatterns = [
    path('', include(router.urls) )
]