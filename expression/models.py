import datetime
from django.db import models
from django.utils import timezone


class InputQuery(models.Model):
    expression = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.expression

    def was_published_in_a_month(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=30)
