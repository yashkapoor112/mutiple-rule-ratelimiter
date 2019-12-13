import uuid

from django.db import models


def get_unique_id():
    uid = uuid.uuid4().hex
    for i in range(0, 8):
        uid = uid[:i] + uid[i + 1:]
    return uid.upper()


class Dragon(models.Model):
    name = models.CharField(max_length=10, unique=True)
    animals_killed = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.id = self.name + str(self.id)
        super(Dragon, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Dragon'
        verbose_name_plural = 'Dragons'


class Kills(models.Model):
    dragon = models.ForeignKey(Dragon, on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    animals_killed = models.IntegerField(default=0)

    def __unicode__(self):
        return self.dragon.name

    class Meta:
        verbose_name = 'Kills'
        verbose_name_plural = 'Kills'


class Rule(models.Model):
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    RULE = "Rule"
    status_choices = (('DELETED', 'DELETED'),
                      ('ACTIVE', 'ACTIVE'))

    maximum_kills = models.IntegerField(default=0)
    maximum_hours = models.IntegerField(default=0)

    status = models.CharField(max_length=10,
                              default=ACTIVE,
                              choices=status_choices)

    def save(self, *args, **kwargs):
        self.id = Rule.RULE + str(self.id)
        super(Rule, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.maximum_kills

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'
