from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo