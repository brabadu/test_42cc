from django.db import models


class RequestLogEntry (models.Model):
    time = models.DateTimeField()
    ip_address = models.CharField(max_length=15)
    url = models.CharField(max_length=50)
    request_method = models.CharField(max_length=10)
    user_agent = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.time.ctime(),
                                            self.ip_address,
                                            self.request_method,
                                            self.url,
                                            self.user_agent,
                                            )

    def equals(self, log_entry):
        if isinstance(log_entry, RequestLogEntry):
            self_time = self.time.timetuple()[:6]
            log_entry_time = log_entry.time.timetuple()[:6]
            return self_time == log_entry_time and \
                   self.ip_address == log_entry.ip_address and \
                   self.url == log_entry.url and \
                   self.request_method == log_entry.request_method and \
                   self.user_agent == log_entry.user_agent
        else:
            raise Exception('RequestLogEntry object expected')
