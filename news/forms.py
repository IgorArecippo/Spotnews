from django import forms
from news.models.category_model import Categories
from news.models.news_model import News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title',
                  'content', 'author', 'created_at', 'image', 'categories']
