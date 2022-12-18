from rest_framework import viewsets
from back.models import Personagem, Habilidades
from back.serializer import PersonagemSerializer, HabilidadesSerializer

class PersonagemViewSet(viewsets.ReadOnlyModelViewSet):
    """Apenas GET dos personagens"""
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

class HabilidadesViewSet(viewsets.ReadOnlyModelViewSet):
    """Apenas GET das habilidades"""
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadesSerializer

