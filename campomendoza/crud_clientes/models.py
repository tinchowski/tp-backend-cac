from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

# https://docs.djangoproject.com/en/5.0/topics/db/models/
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
# https://docs.djangoproject.com/en/4.2/ref/validators/#built-in-validators

class VisitaModel(models.Model):
    PLAN=(
        ('1','Recorrida'),
        ('2','Recorrida y almuerzo'),
        ('3','Solo almuerzo'),
        ('4','Recorrida y cena'),
        ('5','Solo Cena')
    )
    """
    PLAN=(
        {"rec":"Recorrida"},
        {"rec_almuerzo":"Recorrida y almuerzo"},
        {"almuerzo":"Solo almuerzo"},
        {"rec_cena":"Recorrida y cena"},
        {"cena":"Solo cena"},
    )
    """
    fullname = models.CharField(max_length=30,blank=False,verbose_name="Nombre completo")
    cant_personas = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,verbose_name="Cantidad de personas")
    photo = models.FileField(null=False,verbose_name="Foto del DNI")
    email_input = models.EmailField(null=False,verbose_name="Email")
    news = models.BooleanField(default=False,verbose_name="Suscripcion")
    date = models.DateField(null=False,verbose_name="Fecha")
    plan = models.IntegerField(default=1,verbose_name="Plan")
    created = models.DateTimeField(auto_now=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Actualizado")

    def plan_title(self):
        return self.PLAN[self.plan-1][1]

    def news_espanol(self):
        return "Si" if self.news else "No"

    class Meta:
        verbose_name = "visita"
        verbose_name_plural = "Visitas"
        ordering = ["-created"]

# Como reflejar estos modelos a la base de datos

# python manager.py flush
# python manager.py makemigrations crud_clientes
# python manager.py migrate
