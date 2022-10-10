from django.urls import path
from .views import AnimalView, AnimalViewId

urlpatterns = [
    path("animals/", AnimalView.as_view()),
    path("animals/<int:animal_id>", AnimalViewId.as_view()),
]