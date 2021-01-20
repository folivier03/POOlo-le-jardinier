from vegetable import Vegetable
from tomate import Tomate
from potato import Potato
from concombre import Pickle


class Jardinier:
    def get_vegetable(self, vegetable_name):
        if vegetable_name == "tomate":
            return Tomato()
        elif vegetable_name == "potato":
            return Potato()
        elif vegetable_name == "pickle":
            return Pickle()
