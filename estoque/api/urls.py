from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet, basename='produtos')
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')
router.register(r'lotes', views.LoteViewSet, basename='lotes')

urlpatterns = [
    path('', include(router.urls)),
]