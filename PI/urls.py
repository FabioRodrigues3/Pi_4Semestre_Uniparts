"""PI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from venda import views 
from . import settings
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_usuario), 
    path('cadastro/', views.usuario_registro),
    path('cadastro/submit', views.set_usuario),
    path('login/submit', views.submit_login), 
    path('logout/', views.logout_usuario),
    path('feitoLogin/',views.index),
    path('sobre/', views.sobre),
    path('produto/', views.lista_produtos),
    path('produto/pm/', views.lista_placamae),
    path('produto/pr/', views.lista_processador),
    path('produto/pv/', views.lista_placavideo),
    path('produto/dr/', views.lista_discorigido),
    path('produto/fo/', views.lista_fontes),
    path('produto/mr/', views.lista_memoriaram),
    path('produto/finalizar/<id>/', views.finalizar_produto),
    path('produto/finalizar/<id>/submit', views.comprar),
    path('produto/todos', views.lista_produtos),
    path('detalhe/<id>/',views.produto_detail),
    path('detalhe/<id>/submit',views.addcarrinho),
    path('produto/registro/', views.produto_registro),
    path('produto/registro/submit', views.set_produto),
    path('produto/deletar/<id>/', views.deletar_produto),
    path('', RedirectView.as_view(url='produto/')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
