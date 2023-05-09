from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SignUpForm
from website.models import Record

def home(request):
    records = Record.objects.all()
    
    
    # Checar se o usuário está logado
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticação
        user = authenticate(request, username=username, password=password)  # use o email em vez do nome de usuário
        if user is not None:
            login(request, user)
            messages.success(request, "Você logou com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro: Cheque suas crendenciais e me forneça de forma correta")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

# def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Você deslogou da sua conta.")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, "Você se registrou com sucesso! Bem-vindo.")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Olhar por cima dos registros
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "Você precisa estar logado para ver essa página")
        return redirect('home')