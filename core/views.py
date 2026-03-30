from django.shortcuts import render, redirect
from .forms import ClienteForm,EntregaForm
from .models import Cliente,Entrega


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

def nova_entrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)  # 👈 ISSO AQUI

    else:
        form = EntregaForm()

    return render(request, 'nova_entrega.html', {'form': form})

def lista_entregas(request):
    pendentes = Entrega.objects.filter(status='Pendente')
    concluidas = Entrega.objects.filter(status='Entregue')

    return render(request, 'lista_entregas.html', {
        'pendentes': pendentes,
        'concluidas': concluidas
    })

def concluir_entrega(request, id):
    entrega = Entrega.objects.get(id=id)
    entrega.status = 'Entregue'
    entrega.save()
    return redirect('lista_entregas')

def registrar_devolucao(request, id):
    entrega = Entrega.objects.get(id=id)

    if request.method == 'POST':
        isopor = request.POST.get('isopor_devolvido')
        casco = request.POST.get('casco_devolvido')

        # Atualiza valores
        entrega.isopor_devolvido += int(isopor or 0)
        entrega.casco_devolvido += int(casco or 0)

        # Se devolveu tudo → marca como entregue
        if entrega.isopor_pendente == 0 and entrega.casco_pendente == 0:
            entrega.status = 'Entregue'

        entrega.save()
        return redirect('lista_entregas')

    return render(request, 'registrar_devolucao.html', {'entrega': entrega})