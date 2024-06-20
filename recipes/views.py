from .serializers import CategorySerializer, RecipeSerializer, CommentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Recipe, Comment


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('recipes').all()
    serializer_class = CategorySerializer

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.prefetch_related('comments').all()
    serializer_class = RecipeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        recipe = self.get_object()

        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(recipe=recipe)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'GET':
            comments = Comment.objects.filter(recipe=recipe)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)