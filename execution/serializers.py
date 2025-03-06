from rest_framework import serializers
from .models import Projetos, Colaboradores

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'
        
        
class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'