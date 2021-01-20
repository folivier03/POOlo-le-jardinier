from vegetable import Vegetable


class Tomate(Vegetable):
    def grow(self, seed_number=0):
        self.seed_number = seed_number
        return(seed_number)
