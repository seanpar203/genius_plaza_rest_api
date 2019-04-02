# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cooking.models import Recipe
from cooking.serializers import RecipeSerializer
from rest_framework import generics


# Create your views here.
class RecipeList(generics.ListCreateAPIView):
    """
    Recipe List & Create View.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        """ Concrete get_queryset method.

        Notes:
            Used to have custom query params for list filtering.
        """
        queryset = Recipe.objects.all()

        user_id = self.request.query_params.get('user_id')

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recipe Get, Update & Delete View.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
