from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(max_length=100, verbose_name="Descripción")
    image= models.ImageField(verbose_name="Imagen", upload_to = "projects")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación ") #se ejecuta al crearse
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización ") # cada vez que se produce una instancia se actualiza al modificar .

    class Meta:
         verbose_name = " portafolio"
         verbose_name_plural = "proyectos"
         ordering = ["-created"]

    def __str__(self):
        return self.title
