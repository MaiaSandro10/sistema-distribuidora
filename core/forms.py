from django import forms
from .models import Cliente,Entrega

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'endereco']
class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = [
        'cliente',
        'produto',
        'quantidade',
        'data_entrega',
        'isopor_enviado',
        'casco_enviado',
        'status',
        'foto_isopor'
    ]