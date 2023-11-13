from django import template
from Blog.models import Post

from django.db.models import Count

# Para utilizar markdown en el cuerpo del post.
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def posts_totales():
    return Post.objects.count()


@register.inclusion_tag("Blog/ultimos_posts.html")
def mostrar_ultimos_posts(contador=5):
    ultimos_posts = Post.objects.order_by("-created")[:contador]
    return {"ultimos_posts": ultimos_posts}


@register.simple_tag
def obtener_posts_mas_comentados(contador=5):
    return Post.objects.annotate(comentarios_totales=Count("comentarios")).order_by(
        "-comentarios_totales"
    )[:contador]

@register.filter(name='markdown')
def markdown_format(texto):
    return mark_safe(markdown.markdown(texto))
