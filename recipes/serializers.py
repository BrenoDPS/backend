from rest_framework import serializers

from .models import Recipe, Category

class RecipeSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = Recipe
        fields = '__all__'

    
class CategorySerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'
