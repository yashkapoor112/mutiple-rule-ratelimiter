from kills.helpers import get_or_none
from kills.models import *


class RulesAccessor(object):

    def __init__(self, id=None):
        self.id = id

    def get_rule_by_id(self):
        return get_or_none(Rule, id=self.id, status=Rule.ACTIVE)

    def delete_rule_by_id(self):
        rule = self.get_rule_by_id()
        if not rule:
            return None
        rule.status = Rule.DELETED
        rule.save()
        return rule

    def get_all_rules(self):
        return Rule.objects.filter(status=Rule.ACTIVE)

    def get_max_hours_of_all_rules(self):
        rules = Rule.objects.filter(status=Rule.ACTIVE)
        if not rules:
            return None
        return rules.aggregate(Max('maximum_hours'))['maximum_hours__max']