from django.db import models


class Event(models.Model):
    event_name = models.CharField( max_length=200, default="", verbose_name="EVENT NAME")
    event_start = models.DateTimeField(verbose_name="START TIME", null=False)
    event_end = models.DateTimeField(verbose_name="END TIME", null=False)

    def __str__(self):
        return self.event_name


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    ticket_name = models.CharField( max_length=200, verbose_name="TICKET NAME")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, verbose_name="Event")
