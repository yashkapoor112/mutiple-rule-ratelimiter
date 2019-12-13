from kills.helpers import get_or_none
from kills.models import Dragon, Rule


class Setters(object):

    def __init__(self, id=None):
        self.id = id

    def set_dragon(self, dragon_name):
        if dragon_name:
            return Dragon.objects.create(name=dragon_name)
        else:
            return None

    def set_rule(self, maximum_hours, maximum_kills):
        if maximum_kills and maximum_hours:
            return Rule.objects.create(maximum_hours=maximum_hours, maximum_kills=maximum_kills)
        return None

    def update_killed_animals(self, animals_killed):
        dragon = get_or_none(Dragon, id=id)
        if not dragon:
            return None
        dragon.animals_killed = animals_killed
        dragon.save()
        return dragon

    def update_last_timestamp(self, last_timestamp):
        dragon = get_or_none(Dragon, id=id)
        if not dragon:
            return None
        dragon.last_timestamp = last_timestamp
        dragon.save()
        return dragon
