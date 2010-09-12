from django.db.models.signals import post_save
from django.db.models.signals import post_delete

from database_logger.signals import DatabaseChangeLogger

post_save.connect(DatabaseChangeLogger)
post_delete.connect(DatabaseChangeLogger)
