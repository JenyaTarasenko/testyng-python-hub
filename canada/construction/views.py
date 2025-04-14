from typing import Any
from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import send_mail#розсылка
from django.views.generic import DetailView, ListView
from .models import Category, Project, Review
from .utils import send_telegram_message
import random
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .form import UserRegistrationForm, ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# детальная страница категорий 
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    projects = category.projects.all()# Получаем все проекты, связанные с категорией
    return render(request, 'app/pages/category_detail.html', {'category': category,'projects': projects })
    


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Проверка: существует ли уже пользователь с таким username
            if User.objects.filter(username=username).exists():
                messages.info(request, 'A user with this login already exists')
            else:
                User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
                messages.success(request, 'Registration was successful')
                return redirect('construction:index')  # Измени на нужный URL
    else:
        form = UserRegistrationForm()

    return render(request, 'app/pages/registration.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('construction:index')
        else:
            messages.error(request, 'Incorrect login or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'app/pages/login.html', {'form':form})    
      
# страница все проеты рандомные проекты
def project_all(reguest):
    projects = Project.objects.all()
    random_projects = random.sample(list(projects),min(1, len(projects))) # рандомные 2 проекта
    return render(reguest, "app/pages/projects-all.html", {'projects': projects, 'random_projects':random_projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    # reviews = project.reviews.filter(is_published=True)
    project_images = project.images.all()
    reviews = project.reviews.all()
    

    # Если метод POST (форму отправили)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please sign in to leave a review.')
            return redirect('construction:register')  # или имя url на страницу логина

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.user = request.user  # сохраняем ссылку на пользователя
            review.save()
            print("Review saved:", review) 
            messages.success(request, 'Thank you for your feedback! It will be published after verification.')
            return redirect(project.get_absolute_url())
    else:
        form = ReviewForm()
        
    print("User is authenticated:", request.user.is_authenticated)
    print("Username:", request.user.username)       
    return render(request, 'app/pages/project_detail.html', {
        'project': project,
        'reviews': reviews,
        'project_images': project_images,
        'form': form,
    })

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
        reviews = Review.objects.order_by('-id')[:3]

    return render(request, 'app/pages/index.html', {'form': form, 'items':items, 'project_item':project_item, 'reviews': reviews })  # Отправляем форму в шаблон        






# class CategoryDetailView(DetailView):
#     model = Category
#     context_object_name = 'category' 
#     template_name = 'app/category_detail.html' 
    
   
    
    
