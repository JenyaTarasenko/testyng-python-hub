from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории проекта')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-адрес категории")
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'
    
    def __str__(self):
        return self.name  
    
    
class Project(models.Model):
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', verbose_name="Категория")  
    name = models.CharField(max_length=200, verbose_name="Название проекта") 
    slug = models.SlugField(max_length=200,verbose_name="URL-адрес проекта", unique=True)
    description = models.TextField(verbose_name="Описание проекта", blank=True, null=True)  
    image = models.ImageField(upload_to='projects/images/', verbose_name='Фото проекта', blank=True, null=True) 
    video = models.FileField(upload_to='projects/videos/', verbose_name='Видео проета', blank=True, null=True) 
    youtube_url_video = models.URLField(verbose_name='YouTube видео', blank=True, null=True)
    
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['name']),
        ]
        
    def __str__(self):
        return self.name

       
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    comment = models.TextField()
    
    def __str__(self):
        return  self.name