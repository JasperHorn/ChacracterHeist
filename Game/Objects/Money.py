
from .Object import Object

class Money(Object):
    def __init__(self, amount):
        self.amount = amount

    def stepOn(self, player):
        player.addMoney(self.amount)
        self.field.removeObject(self)
