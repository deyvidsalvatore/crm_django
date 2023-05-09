from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Checar se o usuário está logado
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Autenticação
        user = authenticate(request, username=username, password=password)  # use o email em vez do nome de usuário
        if user is not None:
            login(request, user)
            messages.success(request, "Você logou com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro: Cheque suas crendenciais e me forneça de forma correta")
            return redirect('home')
    return render(request, 'home.html', {})

# def login_user(request):
#    pass

# def logout_user(request):
#    pass