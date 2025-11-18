from rest_framework import serializers
from .models import Cidadao

class CidadaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidadao
        fields = '__all__'