from Item_cart import ItemCart


class Catalog:
    def __init__(self,items):
        self.items = items

    def show_items(self):
        print(f"ID товара\t\tНазвание товара\t\tСтоимость товара\t\tКатегория товара")
        for item in self.items:
            print(f"{item.id}\t\t\t\t{item.title}\t\t\t\t\t\t{item.price}\t\t{item.cat.title_cat}")

    def get_item(self,id):
        for item in self.items:
            if item.id == id:
                print("Товар найден")
                return item
        print("Товар не найден")


    def add_item_cart(self, cart):
        while 1:
            id = int(input("Введите ID товара, который добавляем в корзину или -1 для выхода\n"))
            if id == -1:
                break
            item_for_cart = self.get_item(id)
            #Если нашли товар в каталоге по ID, то на его основе построим товар корзины
            if item_for_cart:
                item_cart = ItemCart(id,item_for_cart.title,
                                     item_for_cart.price, item_for_cart.cat)
                cart.add_item(item_cart)
