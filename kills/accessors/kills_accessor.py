import logging
from datetime import timedelta

from kills.accessors.rules_accessor import RulesAccessor
from kills.helpers import get_or_none, get_datetime_object_from_string, get_difference_between_two_dates
from kills.models import *

log = logging.getLogger(__name__)


class KillsAccessor(object):

    def __init__(self, dragon):
        self.dragon = dragon

    def get_all_kills(self):
        return Kills.objects.filter(dragon=self.dragon)

    def get_kills_less_than_timestamp_desc(self, timestamp):
        return Kills.objects.filter(dragon=self.dragon, timestamp__gte=timestamp).order_by('-timestamp')

    def set_kill(self, timestamp, animals_killed):
        if not self.is_kill_possible(timestamp, animals_killed):
            return None, "Kill not possible"

        kill = Kills.objects.create(timestamp=timestamp,
                                    animals_killed=animals_killed,
                                    dragon=self.dragon)
        if not kill:
            return None, "Cannot create kill"
        return kill, "Kill created Successfully"

    def is_kill_possible(self, current_timestamp, number_of_animals_to_be_killed):
        max_hours_of_rules = RulesAccessor().get_max_hours_of_all_rules()
        kills = KillsAccessor(dragon=self.dragon).get_kills_less_than_timestamp_desc(
            current_timestamp - timedelta(hours=max_hours_of_rules))

        rules = RulesAccessor().get_all_rules()
        log.error("Rules {}".format(rules))
        if not rules:
            return True

        total_kills_yet = number_of_animals_to_be_killed
        for kill in kills:
            last_kill_timestamp = kill.timestamp
            time_difference = get_difference_between_two_dates(current_timestamp, last_kill_timestamp)
            total_kills_yet += kill.animals_killed

            for rule in rules:
                if time_difference >= rule.maximum_hours:
                    if not rule.maximum_kills >= number_of_animals_to_be_killed:
                        return False
                elif not (rule.maximum_hours >= time_difference and rule.maximum_kills >= total_kills_yet):
                    return False

        if not kills:
            for rule in rules:
                if not rule.maximum_kills >= total_kills_yet:
                    return False
            return True

        return True
