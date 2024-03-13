from django.db import models
from django.conf import settings


class WorkoutPlan(models.Model):
    GOAL_CHOICES = (
        ("WL", "Weight Loss"),
        ("MG", "Muscle Gain"),
        ("SG", "Strength Gain")
    )
    EXERCISE_TYPES = (
        ("CA", "Cardio"),
        ("GE", "Gym Exercises"),
        ("YO", "Yoga")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.CharField(max_length=2,
                            choices=GOAL_CHOICES)
    frequency_per_week = models.IntegerField()
    exercise_types = models.CharField(max_length=2,
                                      choices=EXERCISE_TYPES)
    session_duration = models.DurationField()


class ExerciseDetails(models.Model):
    """
    Model for saving exercise details of workout plan
    """
    workout_plan = models.ForeignKey(WorkoutPlan,
                                     on_delete=models.CASCADE,
                                     related_name="exercises")
    exercise = models.ForeignKey("exercises.Exercise",
                                 on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(null=True, blank=True)
    sets = models.PositiveIntegerField(null=True, blank=True)
    duration = models.DurationField()
    distance = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )


class WeightCheck(models.Model):
    """
    Model for saving weight by date
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="weight_history")
    current_weight = models.FloatField()
    date_of_weight = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Weight on {self.date_of_weight}'


class FitnessGoal(models.Model):
    """
    Model for setting future goals
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="goals")
    exercise = models.ForeignKey("exercises.Exercise",
                                 on_delete=models.CASCADE,
                                 null=True)
    goal_title = models.CharField(max_length=50)
    current_progress = models.CharField(max_length=150)
    goal = models.CharField(max_length=150)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_title

