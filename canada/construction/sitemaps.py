from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Project


class CategorySitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения страниц
    priority = 0.7  # Приоритет страниц
    
    def items(self):
        return Category.objects.all()
    
    
    def lastmode(self, obj):
        return obj.slug
        
    def location (self, obj):
        return reverse('construction:category_detail', args=[obj.slug])  
    
class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    
    
    def items(self):
        return Project.objects.all()
    
    
    def lastmode(self, obj):
        return obj.slug
    
    def location(self, obj):
        return reverse('construction:project_detail', args=[obj.slug])
        
    
    
    
    
          
        