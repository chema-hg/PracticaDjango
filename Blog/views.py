from django.shortcuts import render, get_object_or_404, get_list_or_404

from . models import Post,Categoria

from django.http import Http404

# Create your views here.

def lista_post(request):
    posts = get_list_or_404(Post)
    categorias = get_list_or_404(Categoria)
    return render(request, 'Blog/lista.html', {'posts': posts, 'categorias': categorias})

# def lista_post(request):
#     posts=Post.objects.all()
#     return render(request, 'Blog/lista.html', {'posts': posts})

# def detalle_post(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("Post no encontrado.")
#     return render(request, 'Blog/detalle.html', {'post': post})


def detalle_post(request, id):
    """Muestra todos los post"""
    post = get_object_or_404(Post, id=id)
    return render(request, 'Blog/detalle.html', {'post': post})

def categoria(request, categoria_id):
    """Muesta una lista de post en base a su categoría"""
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria_id)
    return render(request, 'Blog/categoria.html', {'categoria': categoria, 'posts': posts})