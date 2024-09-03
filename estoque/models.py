from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Base(models.Model):

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Produto(Base):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


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
        return f'{self.produto.nome} - {self.quantidade}'


class Endereco(models.Model):
    rua = models.CharField(max_length=300)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.usuario.nome} - {self.rua} - {self.cidade} - {self.estado} - {self.cep}'

    def atualizarEndereco(self, rua=None, cidade=None, estado=None, cep=None):
        if rua:
            self.rua = rua
        if cidade:
            self.cidade = cidade
        if estado:
            self.estado = estado
        if cep:
            self.cep = cep
        self.save()


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=255)

