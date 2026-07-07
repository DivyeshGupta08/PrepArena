from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    streak = models.PositiveIntegerField(default=0)

    total_attempts = models.PositiveIntegerField(default=0)

    overall_average = models.FloatField(default=0)

    # ------------------------
    # Gamification
    # ------------------------

    xp = models.PositiveIntegerField(default=0)

    level = models.PositiveIntegerField(default=1)

    badges = models.PositiveIntegerField(default=0)

    last_activity = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username