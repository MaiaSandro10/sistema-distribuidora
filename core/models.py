from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
class Entrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data_entrega = models.DateField()
    
    isopor_enviado = models.IntegerField(default=0, blank=True)
    casco_enviado = models.IntegerField(default=0, blank=True)

    isopor_devolvido = models.IntegerField(default=0, blank=True)
    casco_devolvido = models.IntegerField(default=0, blank=True)

    foto_isopor = models.ImageField(upload_to='entregas/', null=True, blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pendente', 'Pendente'),
            ('Entregue', 'Entregue')
        ],
        default='Pendente'
    )

    def __str__(self):
        return f"{self.cliente} - {self.produto}"
    
    @property
    def isopor_pendente(self):
        return self.isopor_enviado - self.isopor_devolvido

    @property
    def casco_pendente(self):
        return self.casco_enviado - self.casco_devolvido