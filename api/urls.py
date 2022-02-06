from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('recipe-list', views.recipeList, name="recipe-list"),
    path('recipe-detail/<str:pk>/', views.recipeDetail, name="recipe-detail"),
    path('recipe-create/', views.recipeCreate, name="recipe-create"),
    path('recipe-update/<str:pk>/', views.recipeUpdate, name="recipe-update"),
    path('recipe-delete/<str:pk>/', views.recipeDelete, name="recipe-delete"),
    path('ingredient-list', views.ingredientList, name="ingredient-list"),
    path('ingredient-detail/<str:pk>/', views.ingredientDetail, name="ingredient-detail"),
    path('ingredient-create/', views.ingredientCreate, name="ingredient-create"),
    path('ingredient-update/<str:pk>/', views.ingredientUpdate, name="ingredient-update"),
    path('ingredient-delete/<str:pk>/', views.ingredientDelete, name="ingredient-delete"),
]
