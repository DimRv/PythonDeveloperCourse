class Cart:
    def __init__(self):
        """Корзина изначально пуста"""
        self.items_cart = []

    def show_items(self):
            print(f"ID товара\t\tНазвание товара\t\tСтоимость товара"
                  f"\t\tКоличество товаров\\Общая стоимость всех товаров")
            for item in self.items_cart:
                print(f"{item.id}\t\t\t\t{item.title}\t\t\t\t\t\t{item.price}"
                      f"\t\t\t\t\t\t\t{item.quantity}\t\t\t\t\t{item.quantity * item.price}")

    def add_item(self,item_cart):
            #Обходим все товары корзины и ищем товар который пытаемся добавить
            for i,item in enumerate(self.items_cart):
                #Если нашли товар с таким ID
                if item.id == item_cart.id:
                    self.items_cart[i].quantity += 1
                    print("Товар добавлен повторно")
                    break
            else:
                self.items_cart.append(item_cart)
                print("Товар добавлен впервые в корзину")