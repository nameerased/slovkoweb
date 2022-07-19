from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=5, db_index=True)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']
