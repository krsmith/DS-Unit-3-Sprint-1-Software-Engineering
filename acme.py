import numpy as np


class Product:

    def __init__(self, name, price=10, weight=20, flammability=.5,
                 identifier=np.random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        stealability = self.price/self.weight
        if stealability < 0.5:
            return "Not so stealable..."
        elif stealability >= 0.5 and stealability < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return "...fizzle."
        elif explode >= 10 and explode < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Class to represent BoxingGlove product"""

    def __init__(self, name):
        super().__init__(self, weight=10)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
