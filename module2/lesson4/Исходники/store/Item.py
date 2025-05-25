class Item:
    """Описание товара каталога"""
    count = 0

    def __init__(self,title,price,cat):
        self.cat = cat
        self.price = price
        self.title = title
        Item.count += 1
        self.id = Item.count