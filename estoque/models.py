from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from abc import ABC, abstractmethod

Usuario = get_user_model()

# Classe base abstrata com métodos focados na lógica de estoque


class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def descricao(self):
        raise NotImplementedError()


class Produto(Base):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def repor_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        self.save()

    def retirar_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            raise ValueError("Estoque insuficiente.")
        self.quantidade_estoque -= quantidade
        self.save()

    def descricao(self):
        return f"{self.nome} - Código: {self.codigo} - Estoque: {self.quantidade_estoque}"


class ProdutoPerecivel(Produto):
    validade = models.DateField()

    def esta_valido(self):
        return self.validade >= timezone.now().date()

    def descricao(self):
        status = "Válido" if self.esta_valido() else "Expirado"
        return f"{self.nome} - Validade: {self.validade} ({status}) - Estoque: {self.quantidade_estoque}"


class Lote(models.Model):
    class TipoUnidade(models.TextChoices):
        unidade = "und", "Unidade"
        gramas = "g", "Gramas"
        kilo = "kg", "Kilos"
        ml = "ml", "Mililitros"
        litro = "l", "Litros"
        caixa = "cx", "Caixa"

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    validade = models.DateField()
    quantidade = models.IntegerField()
    tipo_unidade = models.CharField(
        max_length=100, choices=TipoUnidade.choices, default=TipoUnidade.unidade)

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} {self.tipo_unidade}'

    def esta_valido(self):
        return self.validade >= timezone.now().date()

    def descricao(self):
        status = "Válido" if self.esta_valido() else "Expirado"
        return f"Lote de {self.produto.nome} - Quantidade: {self.quantidade} ({status})"


class Endereco(models.Model):
    rua = models.CharField(max_length=300)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rua}, {self.cidade} - {self.estado}'

    def atualizar_endereco(self, rua=None, cidade=None, estado=None, cep=None):
        if rua:
            self.rua = rua
        if cidade:
            self.cidade = cidade
        if estado:
            self.estado = estado
        if cep:
            self.cep = cep
        self.save()

    def descricao(self):
        return f"{self.rua}, {self.cidade} - {self.estado} - CEP: {self.cep}"


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='perfil_usuario')
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, related_name='perfil_usuario')
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def descricao(self):
        return f"{self.usuario.username} - Telefone: {self.telefone} - Endereço: {self.endereco.descricao()}"
