from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('productname', 'user', 'productbrand', 'productcategory', 'price', 'stockcount', 'createdAt')
    # Champs sur lesquels vous pouvez cliquer pour accéder aux détails de l'enregistrement
    list_display_links = ('productname', 'user')
    # Champs à utiliser pour la recherche dans l'interface d'administration
    search_fields = ('productname', 'productbrand', 'productcategory')
    # Filtrage par les champs spécifiés
    list_filter = ('productbrand', 'productcategory', 'createdAt')
    # Champs en lecture seule
    readonly_fields = ('createdAt', '_id')
    # Pagination : nombre de produits par page dans l'interface d'administration
    list_per_page = 25

    # Configuration du champ de pré-remplissage, si vous avez des slug
    # prepopulated_fields = {'slug': ('productname',)}

admin.site.register(Product, ProductAdmin)
