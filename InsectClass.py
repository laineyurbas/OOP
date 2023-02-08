import random


class Insect:
    def __init__(self):
        self.wingnumber = 2
        self.legnumber = 4
        self.lengthofflight = 0

    def flightlength(self):
        self.lengthofflight = random.randint(1, 10)

    def get_length(self):
        return self.lengthofflight
