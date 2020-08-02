from django.db import models

# Create your models here.


class FilmReview(models.Model):
    comment = models.CharField(max_length=500)
    star_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'douban_test'
