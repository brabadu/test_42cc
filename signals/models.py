from django.db import models


class DatabaseChangeLogEntry (models.Model):
    time = models.DateTimeField()
    model = models.CharField(max_length=50)
    instance_name = models.CharField(max_length=50)
    CHANGE_CHOICES = (
        ('C', 'Creation'),
        ('U', 'Updating'),
        ('D', 'Deleting'),
    )
    change_type = models.CharField(max_length=1, choices=CHANGE_CHOICES)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.time.ctime(),
                                self.model,
                                self.instance_name,
                                self.change_type,
                                )
