from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from Blog.models import Post

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.updated
    
    # def location(self, obj):
    #     return '/blog/%s' % (obj.slug)
    
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'
 
    def items(self):
        return ["Proyecto_web_app:home",
                "Servicios:servicios",
                "Contacto:contacto",
                ] #returning static pages; 
 
    def location(self, item):
        return reverse(item) #returning the static pages URL; 