import sys

from django.core.management.base import NoArgsCommand
from django.db import models


class Command(NoArgsCommand):
    help = 'List all models in project and count object in them'

    def handle_noargs(self, **options):
        output = "\n".join(["%s: %d" % (model_name, count)
                            for model_name, count in self.get_modellist()])
        sys.stdout.write('%s\n' % output)

    def get_modellist(self):
        '''
        Generates list of models and quantity
         of objects of this model
        '''
        result_list = []
        for model in models.get_models():
            count = model.objects.count()
            result_list.append([model._meta.module_name, count])
        return result_list
