# Generated by Django 4.1 on 2024-03-13 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkoutPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "goal",
                    models.CharField(
                        choices=[
                            ("WL", "Weight Loss"),
                            ("MG", "Muscle Gain"),
                            ("SG", "Strength Gain"),
                        ],
                        max_length=2,
                    ),
                ),
                ("frequency_per_week", models.IntegerField()),
                (
                    "exercise_types",
                    models.CharField(
                        choices=[
                            ("CA", "Cardio"),
                            ("GE", "Gym Exercises"),
                            ("YO", "Yoga"),
                        ],
                        max_length=2,
                    ),
                ),
                ("session_duration", models.DurationField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WeightCheck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_weight", models.FloatField()),
                ("date_of_weight", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weight_history",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FitnessGoal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("goal_title", models.CharField(max_length=50)),
                ("current_progress", models.CharField(max_length=150)),
                ("goal", models.CharField(max_length=150)),
                ("achieved", models.BooleanField(default=False)),
                (
                    "exercise",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exercises.exercise",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="goals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("repetitions", models.PositiveIntegerField(blank=True, null=True)),
                ("sets", models.PositiveIntegerField(blank=True, null=True)),
                ("duration", models.DurationField()),
                (
                    "distance",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exercises.exercise",
                    ),
                ),
                (
                    "workout_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercises",
                        to="plans.workoutplan",
                    ),
                ),
            ],
        ),
    ]
