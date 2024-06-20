from django.contrib import admin

from .models import Recipe, Category, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)

# Personalização da exibição da lista de receitas
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rate', 'description', 'category', 'image', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'rate', 'author')
    search_fields = ('name', 'description', 'ingredients', 'preparation')
    raw_id_fields = ('author',)
    inlines = [CommentInline]
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)