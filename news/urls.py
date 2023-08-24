from django.urls import path, include
from news.views import home, news_details, categories_form
from rest_framework.routers import DefaultRouter
from news_rest.views.categories_view import CategoryViewSet
from news_rest.views.users_view import UserViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>/', news_details, name='news-details-page'),
    path('categories/', categories_form, name='categories-form'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]
