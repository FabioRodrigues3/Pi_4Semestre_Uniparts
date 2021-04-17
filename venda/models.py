from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Produto(models.Model):
    PlacaMae = 'PM'
    Processador = 'PR'
    Fonte = 'FO'
    PlacadeVideo = 'PV'
    DiscoRigido = 'DR'
    MemoriaRAM = 'MR'
    TIPO_DE_PRODUTO_CHOICES = [
        (PlacaMae, 'Placa Mãe'),
        (Processador, 'Processador'),
        (Fonte, 'Fonte'),
        (PlacadeVideo, 'Placa de Vídeo'),
        (DiscoRigido, 'Disco Rígido'),
        (MemoriaRAM, 'Memória RAM'),
    ]
    tipo_de_produto = models.CharField(
        max_length=2,
        choices=TIPO_DE_PRODUTO_CHOICES,
        default=PlacaMae,
    )
    nome = models.CharField(max_length = 20)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits = 9, decimal_places = 2)
    qant = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Usuario(models.Model):
    nome = models.CharField(max_length = 40)
    email = models.CharField(max_length = 30)
    login = models.CharField(max_length = 15)
    senha = models.CharField(max_length = 15)
    datanasc = models.DateField(auto_now=True)

    def __str__(self):
        return self.description # pylint: disable=maybe-no-member 
    def is_upperclass(self):
        return self.tipo_de_produto in (self.DiscoRigido, self.MemoriaRAM)  # pylint: disable=maybe-no-member 
class Historico (models.Model): #orderitem
    nome = models.CharField(max_length = 20)
    preco = models.DecimalField(max_digits = 9, decimal_places = 2)
    data = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome # pylint: disable=maybe-no-member 

class Carrinho(models.Model):#order
    ref_code = models.CharField(max_length=15)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Historico)

    def get_cart_items(self):
        return self.items.all() # pylint: disable=maybe-no-member 

    def get_cart_total(self):
        return sum([items.produto.preco for items in self.items.all()]) # pylint: disable=maybe-no-member 

    def __str__(self):
        return '{0} - {1}'.format(self.usuario,self.ref_code)


class Transacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    sucesso = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.order_id
    class Meta:
        ordering = ['-timestamp']
    
class Historia(models.Model):
    nome = models.CharField(max_length = 40)
    Romance = 'RO'
    Drama = 'DR'
    Aventura = 'AV'
    Terror = 'TE'
    TIPO_DE_GENERO_CHOICES = [
        (Romance, 'Romance'),
        (Drama, 'Drama'),
        (Aventura, 'Aventura'),
        (Terror, 'Terror'),
    ]
    tipo_de_genero = models.CharField(
        max_length=2,
        choices=TIPO_DE_GENERO_CHOICES,
        default=Aventura,
    )
    classificacao = models.IntegerField()
    preco = models.DecimalField(max_digits = 9, decimal_places = 2)
    descricao = models.TextField()
    avaliacao = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='historia', default=False)


