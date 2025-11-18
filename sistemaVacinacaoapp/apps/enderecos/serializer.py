from .models import Endereco
from rest_framework import serializers

class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'