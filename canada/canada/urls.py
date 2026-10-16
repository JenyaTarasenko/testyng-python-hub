
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from construction.sitemaps import CategorySitemap, ProjectSitemap 
from django.contrib.sitemaps.views import sitemap
from construction.views import robots_txt
from construction.views import llms_txt
from construction.sitemaps import (
    CategorySitemap,
    ProjectSitemap,
    StaticPagesSitemap
)

sitemaps = {
    "categories": CategorySitemap,
    "projects": ProjectSitemap,
    "pages": StaticPagesSitemap,
}

# sitemaps = {
#     'categories': CategorySitemap,
#     'projects': ProjectSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("llms.txt", llms_txt, name="llms_txt"),
    path('', include('construction.urls', namespace='construction')),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
