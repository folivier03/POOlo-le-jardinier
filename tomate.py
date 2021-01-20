from vegetable import Vegetable


class Tomate(Vegetable):
    def __init__(self, seed_number=0):
        self.seed_number = seed_number

    def grow(self, seed_number):
        self.seed_number += seed_number
        return self.seed_number
