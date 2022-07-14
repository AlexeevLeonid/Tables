from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=100)


class Note(models.Model):
    id_title = models.ForeignKey(Title, on_delete = models.CASCADE)
    text = models.CharField(max_length=100)