from django.db import models

class Trigger(models.Model):
    name  = models.CharField(blank=False,max_length=100)
    lang  = models.CharField(blank=False,max_length=100)

class Student(models.Model):
    score = models.PositiveIntegerField(blank=False, null=False)
