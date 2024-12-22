from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView #для статических страничек сайта


app_name = 'construction'

urlpatterns = [
    path('', views.submith_question, name='index'),
    path('category/<slug:slug>/',views.CategoryDetailView.as_view(), name='category_detail'),
    path('project/<slug:slug>/',views.ProjectDetailView.as_view(), name='project_detail'),
    path('card/', TemplateView.as_view(template_name="app/pages/card.html"), name="card"), #для статических страничек сайта
    path('about/', TemplateView.as_view(template_name="app/pages/about.html"), name="about"), #для статических страничек сайта
    path('detail/', TemplateView.as_view(template_name="app/pages/detail.html"), name="detail"), #для статических страничек сайта
    path('test/', TemplateView.as_view(template_name="app/pages/test.html"), name="test"), #для статических страничек сайта
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)