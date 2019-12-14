from kills.helpers import get_or_none
from kills.models import Dragon


class DragonAccessor(object):

    def __init__(self, id=None):
        self.id = id

    def get_dragon_by_id(self, id):
        """
        Gets a dragon by id.

        :param id:
        :return: Dragon()
        """
        if not id:
            return None
        return get_or_none(Dragon, name=id)




