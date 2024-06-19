from django.contrib import admin

from .models import Recipe, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)

# Personalização da exibição da lista de receitas
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'image', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'author')
    search_fields = ('name', 'description', 'ingredients', 'preparation')
    raw_id_fields = ('author',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)