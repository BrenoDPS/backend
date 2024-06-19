from django.urls import path, include
from recipes import views
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    # path('recipes-list/', views.RecipesList.as_view(), name='recipes-list'),
    path('', include(router.urls)),
]