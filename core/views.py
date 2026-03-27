from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'cadastrar_cliente.html', {'form': form})
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})
def dashboard(request):
    return render(request, 'dashboard.html')