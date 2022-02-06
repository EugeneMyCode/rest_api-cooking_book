from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RecipeSerializer, IngredientSerializer

from .models import Ingredient, Recipe
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'RecipeList': '/recipe-list/',
        'RecipeDetail View': '/recipe-detail/<str:pk>/',
        'RecipeCreate': '/recipe-create/',
        'RecipeUpdate': '/recipe-update/<str:pk>/',
        'RecipeDelete': '/recipe-delete/<str:pk>/',
        'IngredientList': '/ingredient-list/',
        'IngredientDetail View': '/ingredient-detail/<str:pk>/',
        'IngredientCreate': '/ingredient-create/',
        'IngredientUpdate': '/ingredient-update/<str:pk>/',
        'IngredientDelete': '/ingredient-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def recipeList(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recipeDetail(request, pk):
    try:
        recipes = Recipe.objects.get(id=pk)
    except Recipe.DoesNotExist:
        recipes = None
    serializer = RecipeSerializer(recipes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def recipeCreate(request):
    serializer = RecipeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def recipeUpdate(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def recipeDelete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response("Recipe Deleted Successfully")

@api_view(['GET'])
def ingredientList(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ingredientDetail(request, pk):
    ingredients = Ingredient.objects.get(id=pk)
    serializer = IngredientSerializer(ingredients, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ingredientCreate(request):
    serializer = IngredientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def ingredientUpdate(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    serializer = IngredientSerializer(instance=ingredient, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ingredientDelete(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    ingredient.delete()
    return Response("Ingredient Deleted Successfully")