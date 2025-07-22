from django.db import models

class arxivdb(models.Model):
    name = models.CharField(max_length=15)
    surename = models.CharField(max_length=15)
    faculty = models.CharField(max_length=10)
    group = models.CharField(max_length=6)
    grade = models.CharField()

    def __str__(self):
        return self.name

