# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
# from .models import Category, Project


# class CategorySitemap(Sitemap):
#     changefreq = 'weekly'  # Частота изменения страниц
#     priority = 0.7  # Приоритет страниц
    
#     def items(self):
#         return Category.objects.all()
    
    
#     def lastmode(self, obj):
#         return obj.slug
        
#     def location (self, obj):
#         return reverse('construction:category_detail', args=[obj.slug])  
    
# class ProjectSitemap(Sitemap):
#     changefreq = 'monthly'
#     priority = 0.5
    
    
#     def items(self):
#         return Project.objects.all()
    
    
#     def lastmode(self, obj):
#         return obj.slug
    
#     def location(self, obj):
#         return reverse('construction:project_detail', args=[obj.slug])
        
    # def location(self, obj):
    # return f"{settings.SITE_URL}/mars_studio/{obj.slug}/"
    
    # добавить после обновления домен
    # construction/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Category, Project

class StaticPagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "construction:index",
            "construction:about",
            "construction:hardwood",
            "construction:vinyl",
            "construction:laminate",
        ]

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse(
            "construction:category_detail",
            args=[obj.slug],
        )


class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse(
            "construction:project_detail",
            args=[obj.slug],
        )
          
        