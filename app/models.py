from django.db import models


#модель таблицы
class Title(models.Model):
    name = models.CharField(max_length=100)

#модель заметки (связь многое-к-одному с таблицей)
class Note(models.Model):
    id_title = models.ForeignKey(Title, on_delete = models.CASCADE)
    text = models.CharField(max_length=100)