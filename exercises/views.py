from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Exercise
from .serializers import ExerciseSerializer
from .permissions import IsAllowedToRetrieve


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated, IsAllowedToRetrieve)

