from django.shortcuts import render,redirect
from .models import Usuario,Produto,Historico
from .forms import ProdutoForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.


@login_required(login_url='/login/')
def index(request):
    venda = Historico.objects.filter(user=request.user) # pylint: disable=maybe-no-member
    return render(request, 'feitoLogin.html', {'venda':venda})

def logout_usuario(request):
    logout(request)
    return redirect('/login/')
def login_usuario(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/feitoLogin/')
        else:
            messages.error(request,'Usuário e/ou senha inválidas, tenta novamente. ')
            return redirect('/login/')


        


def lista_produtos (request):
    venda = Produto.objects.all() # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )

def lista_placamae(request):
    venda = Produto.objects.filter(tipo_de_produto='PM') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )
    
def lista_processador(request):
    venda = Produto.objects.filter(tipo_de_produto='PR') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )
    
def lista_fontes(request):
    venda = Produto.objects.filter(tipo_de_produto='FO') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )

    
def lista_placavideo(request):
    venda = Produto.objects.filter(tipo_de_produto='PV') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )

    
def lista_discorigido(request):
    venda = Produto.objects.filter(tipo_de_produto='DR') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )

    
def lista_memoriaram(request):
    venda = Produto.objects.filter(tipo_de_produto='MR') # pylint: disable=maybe-no-member
    return render(request,'Home.html',{'venda':venda} )


def criar_produto (request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect ('lista_produtos')
    
    return render ( request,'cadastroProduto.html',{'form' : form})

def atualizar_produto (request, id):
    venda = Produto.objects.get(id=id)  # pylint: disable=maybe-no-member
    form = ProdutoForm(request.POST or None, instance = venda)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'cadastroProduto.html',{'form': form, 'venda': venda})



@login_required(login_url='/login/')
def deletar_produto (request, id):
    venda = Produto.objects.get(id=id)  # pylint: disable=maybe-no-member
    venda.delete()
    
    return redirect('/')

def produto_detail(request, id):
    venda = Produto.objects.get(id=id) # pylint: disable=maybe-no-member
    return render(request,'produtoDetail.html',{'venda': venda})

@login_required(login_url='/login/')
def produto_registro(request):
    produto_id = request.GET.get('id')
    if produto_id:
        venda = Produto.objects.get(id=produto_id) # pylint: disable=maybe-no-member
        return render(request,'cadastroProduto.html', {'venda':venda})
    return render(request,'cadastroProduto.html')

@login_required(login_url='/login/')
def set_produto(request):
    tipoproduto = request.POST.get('tipoproduto')
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')
    qant = request.POST.get('qant')
    imagem = request.FILES.get('imagem')
    produtoid = request.POST.get('venda.id')
    if produtoid:
        venda = Produto.objects.get(id=produtoid)# pylint: disable=maybe-no-member
        print(produtoid)
        venda.tipoproduto = tipoproduto
        venda.nome = nome
        venda.descricao = descricao
        venda.preco = preco
        venda.qant = qant
        if imagem:
            venda.imagem = imagem
        venda.save()
    else: 
        print(produtoid)
        venda = Produto.objects.create(tipo_de_produto=tipoproduto,nome=nome, descricao=descricao, preco=preco,imagem=imagem, qant=qant) # pylint: disable=maybe-no-member
    
    return redirect('/')

def inicio(request):
    return render(request,'Home.html')

def usuario_registro(request):
    return render(request,'cadastro.html')

def set_usuario(request):
    logout(request) 
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    csenha = request.POST.get('csenha')
    if senha == csenha:
        if senha != "":
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            usuario = authenticate(username=nome, password=senha)
            login(request, user)
            return redirect('/feitoLogin/')
        else:
            messages.error(request,'Usuário e/ou senha inválidas, tenta novamente. ')
            return redirect('/cadastro/')
    else:
        messages.error(request,'Usuário e/ou senha inválidas, tenta novamente. ')
        return redirect('/cadastro/')

    return redirect('/')

def addcarrinho(request, id):
    user = request.user 
    return redirect('/')

def sobre(request):
    return render(request, 'sobre.html')
@login_required(login_url='/login/')
def finalizar_produto(request,id):
    venda = Produto.objects.get(id=id) # pylint: disable=maybe-no-member
    return render(request, 'finalizar.html',{'venda': venda})

def comprar(request,id):
    user = request.user
    nome = request.POST.get('venda.nome')
    preco = request.POST.get(('venda.preco'))
    venda = Historico.objects.create(nome=nome, preco=preco,user=user) # pylint: disable=maybe-no-member
    return redirect('/')