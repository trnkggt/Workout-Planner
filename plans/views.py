from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import WorkoutPlanSerializer, ExerciseDetailsSerializer
from .serializers import WeightCheckSerializer, FitnessGoalSerializer
from .models import WorkoutPlan, ExerciseDetails, FitnessGoal, WeightCheck
from .permissions import IsOwnerOfExerciseDetails, IsOwnerOf


class WorkoutPlanViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOf)
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)

        return qs


class ExerciseDetailsViewSet(ModelViewSet):
    queryset = ExerciseDetails.objects.all()
    serializer_class = ExerciseDetailsSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfExerciseDetails)

    def get_queryset(self):
        workout_plan = self.kwargs.get("workout_plan")
        qs = super().get_queryset().filter(workout_plan=workout_plan)
        return qs


class FitnessGoalViewSet(ModelViewSet):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = (IsAuthenticated, IsOwnerOf)

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)
        return qs

    @action(detail=False, methods=['GET'])
    def achieved(self, request):
        """
        Retrieve achieved goals
        """
        queryset = self.queryset.filter(achieved=True)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class WeightCheckViewSet(ModelViewSet):
    queryset = WeightCheck.objects.all()
    serializer_class = WeightCheckSerializer
    permission_classes = (IsAuthenticated, IsOwnerOf)

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)

        return qs
