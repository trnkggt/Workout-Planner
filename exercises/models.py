from django.db import models


class Exercise(models.Model):
    MUSCLE_GROUPS = (
        ("CH", "Chest"),
        ("BK", "Back"),
        ("TP", "Traps"),
        ("CV", "Calves"),
        ("QD", "Quads"),
        ("HM", "Hamstrings"),
        ("BC", "Biceps"),
        ("TC", "Triceps")
    )
    EQUIPMENTS = (
        ("BW", "Body Weight"),
        ("BB", "Barbell"),
        ("DB", "Dumbbell"),
        ("MC", "Machine"),
        ("TM", "Treadmill")
    )
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50,
                                    choices=MUSCLE_GROUPS)
    equipment = models.CharField(max_length=50,
                                 choices=EQUIPMENTS)
    description = models.CharField(max_length=300)
    instructions = models.CharField(max_length=300)

    class Meta:
        unique_together = ("name", "equipment", "muscle_group")
