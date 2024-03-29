"""
URL configuration for PracticaDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, StaticSitemap

sitemaps = {
    'static':StaticSitemap, #add StaticSitemap to the dictionary
    'blog':BlogSitemap #add DynamicSitemap to the dictionary
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Proyecto_web_app.urls')),
    path('servicios/', include('Servicios.urls')),
    path('blog/', include('Blog.urls')),
    path('contacto/', include('Contacto.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('payment/', include('Payment.urls', namespace='payment')),
    path('cupones/', include('Cupones.urls', namespace='cupones')),
    path('tienda/', include('Tienda.urls')),
    path('carro/', include('Carro.urls')),
    path('cuenta/', include('Autentificacion.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('orders/', include('Orders.urls', namespace='orders')),
    path('__debug__/', include('debug_toolbar.urls')),    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)