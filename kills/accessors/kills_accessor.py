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
        """
        Fetch all kills

        :return: <QuerySet[]>
        """
        return Kills.objects.filter(dragon=self.dragon)

    def get_kills_less_than_timestamp_desc(self, timestamp):
        """
        Get all the kills greater than timestamp in desc order

        :param timestamp: DateTimeField
        :return: <QuerySet[]>
        """
        return Kills.objects.filter(dragon=self.dragon, timestamp__gte=timestamp).order_by('-timestamp')

    def set_kill(self, timestamp, animals_killed):
        """
        Creates a kill object for dragon if that kill is possible on the timestamp

        :param timestamp: DateTimeField
        :param animals_killed: Integer
        :return: (Integer, String)
        """
        if not self.is_kill_possible(timestamp, animals_killed):
            return None, "Kill not possible"

        kill = Kills.objects.create(timestamp=timestamp,
                                    animals_killed=animals_killed,
                                    dragon=self.dragon)
        if not kill:
            return None, "Cannot create kill"
        return kill, "Kill created Successfully"

    def is_kill_possible(self, current_timestamp, number_of_animals_to_be_killed):
        """
        Checks if the kill is possible for give timestamp and number of animals

        :param current_timestamp: DateTimeField
        :param number_of_animals_to_be_killed: Integer
        :return: Bool
        """
        max_hours_of_rules = RulesAccessor().get_max_hours_of_all_rules()
        kills = KillsAccessor(dragon=self.dragon).get_kills_less_than_timestamp_desc(
            current_timestamp - timedelta(hours=max_hours_of_rules))

        rules = RulesAccessor().get_all_rules()
        if not rules:
            return True

        total_kills_yet = number_of_animals_to_be_killed

        # Checking if current kill, in combination with last 'n' kills, is possible or not
        # 'n' is number of kills in max time window of given timestamp and max hours of rules
        for kill in kills:
            # getting the time difference between given kill timestamp and last kill
            # to check if the given timestamp lies in the same time window as last kill
            last_kill_timestamp = kill.timestamp
            time_difference = get_difference_between_two_dates(current_timestamp, last_kill_timestamp)
            total_kills_yet += kill.animals_killed

            for rule in rules:
                # if kill is outside of current time window
                if time_difference >= rule.maximum_hours:
                    if not rule.maximum_kills >= number_of_animals_to_be_killed:
                        return False
                # if kill is within time window and number of animals killed can be accomodated then continue
                elif not (rule.maximum_hours >= time_difference and rule.maximum_kills >= total_kills_yet):
                    return False

        # if no kills have taken place till now
        if not kills:
            for rule in rules:
                if not rule.maximum_kills >= total_kills_yet:
                    return False
            return True

        return True
