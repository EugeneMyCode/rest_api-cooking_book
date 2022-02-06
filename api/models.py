from django.db import models

class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    weight_kg = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self) -> str:
        return str(self.title)


class IngredientsList(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ingredient.title
