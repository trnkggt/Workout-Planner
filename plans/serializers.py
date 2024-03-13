from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import ExerciseDetails, WorkoutPlan, FitnessGoal, WeightCheck
from exercises.models import Exercise


class ExerciseDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())

    class Meta:
        model = ExerciseDetails
        fields = ['id', 'repetitions', 'sets',
                  'duration', 'distance', 'exercise']
        depth = 2


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseDetailsSerializer(many=True, required=False)

    class Meta:
        model = WorkoutPlan
        fields = ("goal", "frequency_per_week", "exercise_types",
                  "session_duration", "exercises")

    def create(self, validated_data):
        user = self.context['request'].user
        exercise_details = validated_data.pop("exercises")
        workout_plan = WorkoutPlan.objects.create(user=user,
                                                  **validated_data)

        for record in exercise_details:
            ExerciseDetails.objects.create(
                workout_plan=workout_plan,
                **record
            )

        return workout_plan

    def update(self, instance, validated_data):
        """
        Override update() to be able to update nested objects
        """
        exercises = None
        if "exercises" in validated_data:
            exercises = validated_data.pop("exercises")
        instance = super().update(instance, validated_data)
        if exercises is not None:
            for record in exercises:
                id = record.pop('id')
                detail_object = ExerciseDetails.objects.filter(id=id).update(
                    **record
                )

        return instance


class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        exclude = ("user", )

    def create(self, validated_data):
        fitness_goal = FitnessGoal.objects.create(
            user=self.context['request'].user,
            **validated_data
        )

        return fitness_goal


class WeightCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCheck
        exclude = ('user',)

    def validate(self, attrs):
        weight = attrs['weight']
        if weight < 0 or weight > 220:
            raise ValidationError("Please provide correct body weight")
        return attrs

    def create(self, validated_data):
        weight_check = WeightCheck.objects.create(
            user=self.context['request'].user,
            **validated_data
        )
        return weight_check