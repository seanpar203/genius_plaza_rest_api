# app_name will help us do a reverse look-up latter.
from django.urls import path
from cooking.views import RecipeList, RecipeDetail

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:pk>', RecipeDetail.as_view()),
]
