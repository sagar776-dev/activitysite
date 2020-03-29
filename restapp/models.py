from django.db import models

class User(models.Model):
    real_name = models.CharField(max_length=40)
    tz = models.CharField(max_length=30)

    def __str__(self):
        return self.real_name



class ActivityPeriod(models.Model):
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')

    class Meta:
        unique_together = ('start_time', 'end_time')

    def __unicode__(self):
        return '%s: %s, %s: %s' % ('start_time', self.start_time, 'end_time', self.end_time)

    def __str__(self):
        return self.start_time+' <-> '+self.end_time

