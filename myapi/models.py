from django.db import models

# Create your models here.

class Produit (models.Model):
    libelle = models.CharField("Libelle produit","libelle",max_length=64)
    prix = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.libelle

class Client(models.Model):
    nom = models.CharField("nom du client","nom",max_length=255)
    adresse = models.TextField()
    email = models.EmailField(blank=True,null=True)
    ville=models.CharField("ville",max_length=64)

    def __str__(self):
        return self.nom