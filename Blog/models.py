from django.db import models

from django.contrib.auth.models import User

# Para importar el usuario que esta creando el post

from django.utils import timezone

# Para importar el timezone y establecer la fecha de creación.

from django.urls import reverse

# Para crear la Url canónica


# Create your models here.
class Categoria(models.Model):
    """Diferentes tags para asignar a los post"""

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='created')
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    categorias = models.ManyToManyField(Categoria, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Model meta Options - https://docs.djangoproject.com/en/4.1/topics/db/models/#meta-options
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['updated']),
        ]

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("Blog:detalle_post", 
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comentarios')
    email = models.EmailField()
    cuerpo = models.TextField(max_length=400)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]
    
    def __str__(self):
        return f"Comentario de {self.autor} en {self.post}"