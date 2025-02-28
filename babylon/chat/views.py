from .models import Message
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, "chat/chat.html", {'messages':messages})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('chat')  # Redireciona para o chat após o registro
    else:
        form = RegisterForm()
    return render(request, 'chat/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')  # Redireciona para a página do chat após o login
    else:
        form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(user=request.user, content=content)
    return redirect('chat')
