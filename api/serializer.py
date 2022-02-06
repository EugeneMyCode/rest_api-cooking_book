from rest_framework import fields, serializers
from .models import IngredientsList, Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Recipe
        fields = '__all__'


class IngredientListSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer
    recipe = RecipeSerializer
    
    class Meta:
        model  = IngredientsList
        fields =("ingredient", "recipe")

