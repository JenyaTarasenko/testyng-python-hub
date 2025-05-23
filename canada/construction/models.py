from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории проекта')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-адрес категории")
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)
    image = models.ImageField(upload_to='categories/images/', verbose_name='Фото категории', blank=True, null=True)
    technologies = models.TextField(verbose_name="Технологии категории", blank=True, null=True)
    
    def get_absolute_url(self):
      return reverse('construction:category_detail', kwargs={"slug": self.slug})

    
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
    
    
    def get_absolute_url(self):
         return reverse("construction:project_detail", kwargs={"slug": self.slug})
    
    
    
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
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="Проект") 
    image = models.ImageField(upload_to='projects/images/', verbose_name='Изображение проекта')   
    
    
    def __str__(self):
        return f"Изображение для {self.project.name}"    
    
    
    
    
class Review(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='reviews', verbose_name="Проект")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    content = models.TextField(verbose_name="Содержание отзыва")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    
    def __str__(self):
        if self.user:
            return f"{self.user.first_name}{self.user.username}"
        else:
            return f"Нет пользователя"
      