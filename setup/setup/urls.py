from django.contrib import admin
from django.urls import path, include
from back.views import PersonagemViewSet, HabilidadesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('personagens', PersonagemViewSet, basename='Personagens')
router.register('habilidades', HabilidadesViewSet, basename='Habilidades')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
