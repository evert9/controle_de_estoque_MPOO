from rest_framework.viewsets import ModelViewSet
from ..models import *
from .serializers import *

class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    def get_queryset(self):
        return Produto.objects.all()
    
class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        return Usuario.objects.all()
    
class LoteViewSet(ModelViewSet):
    serializer_class = LoteSerializer
    def get_queryset(self):
        return Lote.objects.all()