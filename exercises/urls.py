from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("list", views.ExerciseViewSet, basename="exercise")


urlpatterns = [
    path("", include(router.urls)),
    path("list/muscle_group/", views.ExerciseViewSet.muscle_group,
         name='exercise-muscle-group'),
    path("list/equipment/", views.ExerciseViewSet.equipment,
         name='exercise-equipment')
]