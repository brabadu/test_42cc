import datetime

from database_logger.models import DatabaseChangeLogEntry


def DatabaseChangeLogger(sender, **kwargs):
    if str(sender._meta) == str(DatabaseChangeLogEntry._meta):
        return

    time = datetime.datetime.now()
    model = sender._meta.object_name
    instance_name = kwargs['instance']
    change_type = ''
    if 'created' in kwargs:
        change_type = kwargs['created'] and 'Creation' or 'Updating'
    else:
        change_type = 'Deleting'

    DatabaseChangeLogEntry.objects.create(
        time=time,
        model=model,
        instance_name=instance_name,
        change_type=change_type,
    )
