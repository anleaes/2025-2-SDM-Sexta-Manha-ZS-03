from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'unidade'

router = routers.DefaultRouter()
router.register('', views.UnidadeViewSet, basename='unidade')

urlpatterns = [
    path('', include(router.urls) )
]
