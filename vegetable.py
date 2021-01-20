import abc


class Vegetable (abc.ABC):
    """Vegetable est une classe abstraite ."""
    @abc.abstractmethod
    def grow(self, seed_number=0):
        pass


# class Tomate(Vegetable):
#     def grow(self, seed_number=0):
#         return(seed_number)


# tomate = Tomate().grow(5)
# print(tomate)
