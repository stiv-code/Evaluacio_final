from django.db import models

# Create your models here.
class Candidatos(models.Model):
    id_can = models.CharField(max_length=10, blank=True, primary_key=True)
    nombre_can = models.CharField(max_length=100, blank=True)
    apellido_can = models.CharField(max_length=100, blank=True)
    email_can = models.CharField(max_length=100, blank=True)
    telefono_can = models.CharField(max_length=10, blank=True)
    fecha_nac_can = models.DateField(blank=True, null=True)
    genero_can = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.nombre_can} {self.apellido_can}'

class Vacantes(models.Model):
    id_vac = models.CharField(max_length=10, blank=True, primary_key=True)
    nom_vac = models.CharField(max_length=30, blank=False)
    id_can = models.ForeignKey(Candidatos, on_delete=models.RESTRICT)  

    def __str__(self):
        return self.nom_vac

class Locales(models.Model):
    id_loc = models.CharField(max_length=10, blank=True, primary_key=True)
    nombre_loc = models.CharField(max_length=50, blank=False)
    direccion_loc = models.CharField(max_length=100, blank=False)
    id_vac = models.ForeignKey(Vacantes, on_delete=models.RESTRICT)  

    def __str__(self):
        return self.nombre_loc

class Contrato(models.Model):
    id_con = models.CharField(max_length=10, blank=True, primary_key=True)
    fecha_ini_con = models.DateField(blank=False)
    fecha_fin_con = models.DateField(blank=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)  
    id_loc = models.ForeignKey(Locales, on_delete=models.RESTRICT) 
    id_can = models.ForeignKey(Candidatos, on_delete=models.RESTRICT)  
    id_emp = models.ForeignKey(Vacantes, on_delete=models.RESTRICT)  

    def __str__(self):
        return f'Contrato {self.id_con}'