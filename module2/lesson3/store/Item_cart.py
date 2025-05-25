from Item import Item


class ItemCart(Item):
    def __init__(self,id,title,price,cat):
        super().__init__(title,price,cat)
        self.quantity = 1
        self.id = id