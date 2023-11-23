from django.db import models

# Create your models here.
# vai herdar models.Model
class Fotografia(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    preco = models.CharField(max_length=30,null=False,blank=False)
    foto = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
