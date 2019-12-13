from kills.models import *

class DragonBuilder:
    def __init__(self):
        self.name = "Drogon"
        self.dragon = Dragon.objects.create(name = self.name)

    def get_dragon(self):
        self.dragon.save()
        return self.dragon
