from django.urls import path
from . import views

app_name = 'construction'

urlpatterns = [
    path('', views.submith_question, name='index'),
    #  path('', views.index, name="index"),
]