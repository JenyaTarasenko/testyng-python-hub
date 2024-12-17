from django.contrib import admin
from .models import Category,Project
from .models import ContactForm as ContactFormModel

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image', 'video', 'youtube_url_video']
    prepopulated_fields = {'slug':('name',)}


@admin.register(ContactFormModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'comment']

