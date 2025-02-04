from django.db import models

class  Estado(models.Model):
     nome = models.CharField(max_length=50)
     sigla = models.CharField(max_length=2)

     def __str__(self):
          return f"{self.nome} ({self.sigla})"

class Cidade(models.Model): 
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def _str_(self):
         return f"{self.nome} ({Estado.sigla})"

class Pessoa(models.Model):
     nome = models.CharField(max_length=100)
     telefone = models.CharField(max_length=11)
     email = models.EmailField(max_length=50)
     datanasc = models.DateField(max_length=6)