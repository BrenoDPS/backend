from django.urls import path, include
from recipes import views
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RecipesViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]