from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post, Categoria

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

# Create your views here.

class lista_post(ListView):
    """
    Una alternativa a la función lista_post
    """
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "Blog/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


# def lista_post(request):
#     posts = get_list_or_404(Post)
#     categorias = get_list_or_404(Categoria)
#     # Paginación con 3 post por página.
#     paginador = Paginator(posts, 3)
#     numero_pagina = request.GET.get('page', 1)
#     try:
#         posts_por_pagina = paginador.page(numero_pagina)
#     except EmptyPage:
#         # Si la página está fuera del rango de las paginas de resultados
#         posts_por_pagina = paginador.page(paginador.num_pages)
#     except PageNotAnInteger:
#         # Si el párametro introducido no es un número entero
#         posts_por_pagina = paginador.page(1)
#     return render(
#         request, "Blog/lista.html", {"posts": posts_por_pagina, "categorias": categorias}
#     )


def detalle_post(request, year, month, day, post):
    """Muestra todos los post"""
    post = get_object_or_404(
        Post, 
        slug=post, 
        created__year=year, 
        created__month=month, 
        created__day=day,
    )
    return render(request, "Blog/detalle.html", {"post": post})


def categoria(request, categoria_id):
    """Muesta una lista de post en base a su categoría"""
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria_id)
    return render(
        request, "Blog/categoria.html", {"categoria": categoria, "posts": posts}
    )
