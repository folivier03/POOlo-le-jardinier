from vegetable import Vegetable


class Garden():
    def __init__(self):
        self.seed = 0

    def _plant(self, vegetable):
        self.seed += vegetable.seed_number
        return vegetable

    def add(self, vegetable):
        return self._plant(vegetable)
