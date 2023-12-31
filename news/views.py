from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Users, Categories
from news.forms import CategoryForm, NewsForm


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news_details.html', context)


def home(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'home.html', context)


def categories_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'categories_form.html', context)


def news_form(request):
    users = Users.objects.all()
    categories = Categories.objects.all()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = NewsForm()

    context = {'form': form, 'users': users, 'categories': categories}
    return render(request, 'news_form.html', context)
