from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap


app_name = 'construction'

urlpatterns = [
    path('', views.submith_question, name='index'),
    path('category/<slug:slug>/',views.CategoryDetailView.as_view(), name='category_detail'),
    path('project/<slug:slug>/',views.ProjectDetailView.as_view(), name='project_detail'),

]