from django.db import models

# Create your models here.

class Film(models.Model):
    titre = models.CharField(max_length=200)
    synopsis = models.TextField(blank=True)
    prix_location = models.DecimalField(max_digits=5, decimal_places=2)
    nombre_exemplaires = models.IntegerField(default=1)
    est_disponible = models.BooleanField(default=True)
    date_sortie = models.DateField(null=True, blank=True)
    code_reference = models.CharField(max_length=10, unique=True, default="DEFAULT123")
    realisateur = models.ForeignKey('Realisateur', on_delete=models.SET_NULL, null=True, blank=True)
 

    def __str__(self):
        return self.titre
    
class Realisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    biographie = models.TextField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"    

# ِCDI integrité Desponibilité confidentialité