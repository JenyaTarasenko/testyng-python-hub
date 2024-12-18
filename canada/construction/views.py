from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import send_mail#розсылка
from django.views.generic import DetailView
from .models import Category, Project

# def submith_question(request):
#     if request.method == "POST":
#         form =ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
            
            
#             name = form.cleaned_data['name']  
#             number = form.cleaned_data['number']  
#             comment = form.cleaned_data['comment']  
            
#             send_mail(
                
#                 subject=f'Новое сообщение от {name}', 
#                 message=f'Получено новое сообщение от {name} ({number}):\n\n{comment}', 
#                 from_email='jenyatarasenko07@gmail.com',  
#                 recipient_list=['jenyatarasenko07@gmail.com'], 
#                 fail_silently=False,
#             )
#             return redirect('construction:index') 
#     else:
#         form = ContactForm()
#     return render(request, 'app/index.html', {'form':form})    
        

def submith_question(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные формы в базу данных
            form.save()

            # Получаем данные из формы
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            comment = form.cleaned_data['comment']

            # Отправляем письмо
            send_mail(
                subject=f'Новое сообщение от {name}',  # Тема письма
                message=f'Получено новое сообщение от {name} номер отправителя: -{number} сообщение отправителя:-{comment}',  # Текст письма
                from_email='jenyatarasenko07@gmail.com',  # Ваш email
                recipient_list=['jenyatarasenko07@gmail.com'],  # Получатели
            )
            return redirect('construction:index')  # Перенаправление на другую страницу

    else:
        form = ContactForm()  # Если метод GET, то создаем пустую форму
        # items = Category.objects.all()
        # project_item = Project.objects.all()

    return render(request, 'app/index.html', {'form': form})  # Отправляем форму в шаблон        




class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category' 
    template_name = 'app/category_detail.html' 
    
    
    
class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project' 
    template_name = 'app/project_detail.html' 