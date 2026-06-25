from django.db import models


class StudyResource(models.Model):

    topic_name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=200
    )

    url = models.URLField()

    def __str__(self):
        return self.title