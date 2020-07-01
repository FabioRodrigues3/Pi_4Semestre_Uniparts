from django.urls import path
from .views import lista_produtos, criar_produto, atualizar_produto, deletar_produto

urlpatterns = [
    path ('',lista_produtos, name = 'lista_produtos' ),
    path ('Novo', criar_produto, name = 'criar_produto'),
    path ('atualizar/<int:id>/', atualizar_produto, name = 'atualizar_produto'),
    path ('deletar/<int:id>/', deletar_produto, name = 'deletar_produto'),
]