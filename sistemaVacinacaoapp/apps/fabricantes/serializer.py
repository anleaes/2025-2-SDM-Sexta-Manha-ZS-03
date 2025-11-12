from .models import Fabricante
from rest_framework import serializers

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'
