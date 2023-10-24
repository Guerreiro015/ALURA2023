from django.shortcuts import render
from apps.usuarios.forms import LoginForms
from apps.usuarios.forms import CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages

def login(request):
        form = LoginForms()

        if request.method == 'POST':
            form = LoginForms(request.POST)

            if form.is_valid():
                nome=form['nome_login'].value()
                senha=form['senha'].value()


            usuario = auth.authenticate(
               request,
               username=nome,
               password=senha
   )
            
            if usuario is not None:
               auth.login(request, usuario)

            if usuario is not None:
               auth.login(request, usuario)
               messages.success(request, f'{nome} Logado com Sucesso')
               return redirect ('index')

            else:
               messages.warning(request, f'Usuário {nome}, não foi possível logar')
               return redirect('login')

        
        return render(request, "usuarios/login.html", {"form": form})  # Este codigo e para mostrar o formulário feito no arquivo form


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
       form = CadastroForms(request.POST)

       if form.is_valid():        
          # Vamos criar variaveis com os dados do formulário
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()
            senha_2=form['senha_2'].value()
            

            if User.objects.filter(username=nome).exists(): # verifiando se o usuário ja existe
               messages.error(request, f"Usuário {nome}, já existe!")
               return redirect('cadastro')
            if nome:
               nome = nome.strip()
               if ' ' in nome:
                  messages.info(request, f'Espaços não são permitidos no campo Nome de Cadastro')
                  return redirect('cadastro')
               

            if senha != senha_2:
                  messages.error(request, f'Senhas não são iguais')
                  return redirect('cadastro')
                   

            messages.success(request, f"Usuário {nome} cadastrado com sucesso!!!")            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            return redirect('login')
       

   

    return render(request, 'usuarios/cadastro.html', {'form': form}) # Este codigo e para mostrar o formulário feito no arquivo form

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso")
    return redirect('login')
