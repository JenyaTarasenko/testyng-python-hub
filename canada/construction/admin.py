from django.contrib import admin
from .models import Category,Project,ProjectImage
from .models import ContactForm as ContactFormModel


class ProductImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
    fk_name = 'project'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name', 'slug','image','technologies']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'technologies')
    
    # def short_technology(self, obj):
    #     if obj.technologies:  # Проверяем, что поле не пустое
    #         return obj.technologies[:50] + "..." if len(obj.technologies) > 50 else obj.technologies
    #     return "-"
    
    # short_technology.short_description = "Technologies"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'image']
    list_filter = ('category',)
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]  # Добавляем инлайн для изображений
    
    
    


@admin.register(ContactFormModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'comment']
    search_fields = ('name', 'number')
    
    
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):  
    list_display = ['project', 'image']
    list_filter = ('project',)  



