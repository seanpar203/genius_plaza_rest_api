from rest_framework import serializers
from cooking.models import Recipe, Ingredient, Step


class StepSerializer(serializers.ModelSerializer):
    """ Serializer for Step Model. """

    class Meta:
        model = Step
        fields = ('order', 'step_text')


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for Ingredient Model. """

    class Meta:
        model = Ingredient
        fields = ('text',)


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for Recipe Model. """
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('user', 'name', 'steps', 'ingredients')

    def create(self, validated_data):
        """ Custom create method to allow for adding Steps and Ingredients in a single post. """
        steps_data = validated_data.pop('steps', None)
        ingredients_data = validated_data.pop('ingredients', None)

        recipe = Recipe.objects.create(**validated_data)

        if ingredients_data:
            Ingredient.objects.bulk_create([
                Ingredient(recipe_id=recipe.id, **ingredient) for ingredient in ingredients_data
            ])

        if steps_data:
            Step.objects.bulk_create([
                Step(recipe_id=recipe.id, **step) for step in steps_data
            ])

        return recipe
