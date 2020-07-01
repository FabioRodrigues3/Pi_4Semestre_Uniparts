from django import forms
from .models import Produto, Usuario

class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['tipo_de_produto','nome','descricao','preco','qant','imagem']