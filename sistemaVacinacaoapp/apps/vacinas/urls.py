from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vacina'

router = routers.DefaultRouter()
router.register('', views.VacinaViewSet, basename='vacina')

urlpatterns = [
    path('', include(router.urls) )
]
