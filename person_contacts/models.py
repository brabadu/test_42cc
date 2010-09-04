from django.db import models


class Person (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.TextField()
    telephone = models.CharField(max_length=13)
    email = models.EmailField()
    twitter = models.CharField(max_length=15)

    def __unicode__(self):
        return ("%s %s." % (self.last_name, self.first_name[0])).title()
