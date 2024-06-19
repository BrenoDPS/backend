from django.shortcuts import render

from .serializers import CategorySerializer, RecipeSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Recipe


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('recipes').all()
    serializer_class = CategorySerializer

# class RecipesViewSet(viewsets.ModelViewSet):
#     # def get(self, request, format=None):
#         queryset = Recipe.objects.all()
#         serializer = RecipeSerializer(queryset, many=True)
#         # return Response(serializer.data)