from django.db.models import Max

from kills.helpers import get_or_none
from kills.models import *


class RulesAccessor(object):

    def __init__(self, id=None):
        self.id = id

    def get_rule_by_id(self):
        """
        Gets a rule by id

        :return: Rule()
        """
        return get_or_none(Rule, id=self.id, status=Rule.ACTIVE)

    def delete_rule_by_id(self):
        """
        Deletes a rule by id

        :return: Rule()
        """
        rule = self.get_rule_by_id()
        if not rule:
            return None
        rule.status = Rule.DELETED
        rule.save()
        return rule

    def get_all_rules(self):
        """
        Fetch all active rules

        :return: <QuerySet[]>
        """
        return Rule.objects.filter(status=Rule.ACTIVE)

    def get_max_hours_of_all_rules(self):
        """
        Get the maximum of maximum_hours for all the rules

        :return: Integer
        """
        rules = Rule.objects.filter(status=Rule.ACTIVE)
        if not rules:
            return None
        return rules.aggregate(Max('maximum_hours'))['maximum_hours__max']