from typing import Any
from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import send_mail#розсылка
from django.views.generic import DetailView, ListView
from .models import Category, Project
from .utils import send_telegram_message
import random
from django.shortcuts import render, get_object_or_404


# детальная страница категорий 
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    projects = category.projects.all()# Получаем все проекты, связанные с категорией
    return render(request, 'app/pages/category_detail.html', {'category': category,'projects': projects })
    




# главная страничка
# class HomeView(ListView):
#     model = Project
#     context_object_name = 'projects' 
#     template_name = 'app/pages/index.html'
    
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all()
#         return context

# страница все проеты рандомные проекты
def project_all(reguest):
    projects = Project.objects.all()
    random_projects = random.sample(list(projects),min(1, len(projects))) # рандомные 2 проекта
    return render(reguest, "app/pages/projects-all.html", {'projects': projects, 'random_projects':random_projects})


class ProjectDetailView(DetailView):
    model = Project
    template_name = "app/pages/project_detail.html"
    context_object_name = "project"
    
    def get_context_data(self, **kwargs):# все изображения текущий модели
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['project_images'] = project.images.all()
        return context


# страница все категории 
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/pages/category_list.html',{'categories': categories})


def submith_question(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные формы в базу данных
            contact=form.save()

            # Получаем данные из формы
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            comment = form.cleaned_data['comment']

            # Отправляем письмо
            send_mail(
                subject=f'Новое сообщение от {name}',  # Тема письма
                message=f'Получено новое сообщение от {name} номер отправителя: -{number} сообщение отправителя:-{comment}',  # Текст письма
                from_email='torontosergey62@gmail.com',  # Ваш email
                recipient_list=['torontosergey62@gmail.com'],  # Получатели
            )
            
            send_telegram_message(contact) 
            return redirect('construction:index')  # Перенаправление на другую страницу

    else:
        form = ContactForm()  # Если метод GET, то создаем пустую форму
        items = Category.objects.all()
        project_item = Project.objects.all()

    return render(request, 'app/pages/index.html', {'form': form, 'items':items, 'project_item':project_item})  # Отправляем форму в шаблон        






# class CategoryDetailView(DetailView):
#     model = Category
#     context_object_name = 'category' 
#     template_name = 'app/category_detail.html' 
    
   
    
    
