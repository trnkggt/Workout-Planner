from rest_framework.routers import SimpleRouter
from django.urls import path, include

from . import views


router = SimpleRouter()
router.register("list",
                views.WorkoutPlanViewSet,
                basename="workout_plan")
router.register("list/(?P<workout_plan>[^/.]+)/exercise",
                views.ExerciseDetailsViewSet,
                basename="workout_plan_exercise")
router.register("fitness/goal",
                views.FitnessGoalViewSet,
                basename="fitness_goal")
router.register("weight/check",
                views.WeightCheckViewSet,
                basename="weight_check")

urlpatterns = [
    path("fitness/goal/achieved",
         views.FitnessGoalViewSet.achieved,
         name="achieved_goals"),
    path("", include(router.urls))
]
