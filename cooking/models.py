# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Recipe(models.Model):
    """ Represents a cooking recipe which contains steps and ingredients. """
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    """ Represents a single ingredient. """
    text = models.CharField(max_length=255, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f'{self.text}'


class Step(models.Model):
    """ Represents a single step of a recipe. """
    order = models.SmallIntegerField()
    step_text = models.CharField(max_length=255, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')

    def __str__(self):
        return f'{self.order}: {self.step_text}'

    class Meta:
        ordering = ['-order']
