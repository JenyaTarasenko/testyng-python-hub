from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView #для статических страничек сайта


app_name = 'construction'

urlpatterns = [
  
    path('', views.submith_question, name='index'),
    path('category-detail-page/', views.category_list, name="category_list"), #все категории
    path('projects-all/', views.project_all, name="projects_all"), #все проекты
    path('project/<slug:slug>/',views.ProjectDetailView.as_view(), name='project_detail'),
    path('category-detail/<slug:slug>/', views.category_detail, name="category_detail"),
    path('diverse/', TemplateView.as_view(template_name="app/pages/questions.html"), name="questions"), #для статических страничек сайта diverse
    path('about/', TemplateView.as_view(template_name="app/pages/about.html"), name="about"), #для статических страничек сайта about 
    path('gallery/', TemplateView.as_view(template_name="app/pages/gallery.html"), name="gallery"), #для статических страничек сайта gallery
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)