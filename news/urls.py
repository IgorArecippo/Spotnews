from django.urls import path, include
from news.views import home, news_details, categories_form
from rest_framework.routers import DefaultRouter
from news_rest.views.categories_view import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>/', news_details, name='news-details-page'),
    path('categories/', categories_form, name='categories-form'),
    path('api/', include(router.urls)),
]
