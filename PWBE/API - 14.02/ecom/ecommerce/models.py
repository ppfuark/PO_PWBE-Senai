from django.db import models

class Product(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='images/', null=True) 

    def __str__(self):
        return self.titulo