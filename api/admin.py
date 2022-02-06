from django.contrib import admin

from api.models import Recipe, Ingredient, IngredientsList

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientsList)

