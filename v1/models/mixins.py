from django.utils import timezone
from django.db import models


class TimestampQueryset(models.QuerySet):
    def delete(self):
        return super(TimestampQueryset, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(TimestampQueryset, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class TimestampManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(TimestampManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return TimestampQueryset(self.model).filter(deleted_at=None)
        TimestampQueryset(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)

    objects = TimestampManager()
    all_objects = TimestampManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(TimestampMixin, self).delete()
