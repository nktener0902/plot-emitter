import datetime
from django.db import models
from django.utils import timezone


class InputQuery(models.Model):
    pub_date = models.DateTimeField('date published')
    expression = models.CharField(max_length=200)
    noise_function = models.CharField(max_length=20)
    noise = models.FloatField(null=True)
    fineness = models.FloatField()
    x_min_range = models.FloatField()
    x_max_range = models.FloatField()
    comment = models.CharField(max_length=400, null=True, default='')

    def __str__(self):
        return self.expression

    def was_published_in_a_month(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=30)
