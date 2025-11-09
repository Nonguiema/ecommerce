from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image_tag', 'created_at')
    readonly_fields = ('image_tag',)  # Permet de voir l'image dans le formulaire sans l'éditer
    search_fields = ('name',)
    list_filter = ('created_at',)

    # Méthode pour afficher la miniature
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="object-fit: cover;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
