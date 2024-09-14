from rest_framework import serializers
from ..models import Endereco, Lote, PerfilUsuario, Usuario, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = PerfilUsuario
        fields = ['telefone', 'endereco']


class UsuarioSerializer(serializers.ModelSerializer):
    perfil_usuario = PerfilUsuarioSerializer()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password', 'perfil_usuario']
