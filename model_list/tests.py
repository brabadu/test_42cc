from tddspry.django import DatabaseTestCase
from django.db import models
from django.contrib.contenttypes.models import ContentType

from management.commands.modellist import Command


class CommandTest(DatabaseTestCase):
    def test_count(self):
        """
        Tests returned cortage contains only model names
        and numbers of objects are equal or greater then 0
        """

        command = Command()
        modellist = command.get_modellist()
        for model_name, count in modellist:
            # taking model class by it's name
            model = ContentType.objects.get(model=model_name).model_class()
            # testing we've counted objects in this model right
            self.assert_count(model, count)
