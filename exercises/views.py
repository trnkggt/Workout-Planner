from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import Exercise
from .serializers import ExerciseSerializer
from .permissions import IsAllowedToRetrieve


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated, IsAllowedToRetrieve)

    def get_queryset(self):
        qs = super().get_queryset()

        return qs

    @action(detail=False, methods=['GET'])
    def muscle_group(self, request):
        """
        Retrieve exercises by muscle group.
        """
        muscle_group = request.query_params.get('muscle_group')
        queryset = self.queryset.filter(muscle_group=muscle_group.title())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def equipment(self, request):
        """
        Retrieve exercises by equipment type
        """
        equipment = request.query_params.get("equipment")
        queryset = self.queryset.filter(equipment=equipment.title())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

