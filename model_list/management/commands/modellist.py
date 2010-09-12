import sys

from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'List all models in project and count object in them'

    def handle_noargs(self, **options):
        sys.stdout.write('\n')

    def get_modellist(self):
        pass
