class Item:
    def __init__(self, title,content):
        self.title = title
        self.content = content
    def __str__(self):
        return self.title

class Channel:
    def __init__(self, title,items = []):
        self.title = title
        self.items = items
        self.subscribers = []

    def show_info(self):
        print(f"На канале {self.title} размещены видео ролики:")
        # print(", ".join(list(map(lambda item:item.title,self.items))))
        for i,item in enumerate(self.items,1):
            print(f"{i}. {item}")

    def subscribe(self,subscriber):
        """Подписка на канал"""
        self.subscribers.append(subscriber)
        print(f"{subscriber.login}, Вы успешно подписаны на канал")

    def unsubscribe(self,subscriber):
        """Покидаем канал"""
        if self.subscribers:
            for i,item in enumerate(self.subscribers):
                if subscriber.login == item.login:
                    print(f"{self.subscribers.pop(i).login} успешно покинули канал")
                    break
            else:
                print("Подписчик не найден")

    def add_item(self,item):
        """Добавление нового ролика"""
        self.items.append(item)
        for subscriber in self.subscribers:
            subscriber.notify(f'{subscriber.login}, на канале {self.title} вышел ролик'
                              f'{item.title}')

class Subscriber:
    def __init__(self,login):
        self.login = login
    def notify(self,info):
        print(info)

#*************Запуск проекта****************

movie_first = Item("Основы Python","Содержимое ролика 1")
movie_second = Item("Основы JS","Содержимое ролика 2")
movie_third = Item("Основы Django","Содержимое ролика 3")

my_channel = Channel('Блог программиста',[movie_first,movie_second,movie_third])
print("Базовая версия канала")
my_channel.show_info()

subscriber_first = Subscriber('Вася')
subscriber_second = Subscriber('Петя')
subscribers = [subscriber_first,subscriber_second]

for subscriber in subscribers:
    my_channel.subscribe(subscriber)


my_channel.add_item(Item('Всё о микросервисах','Содержимое ролика...'))
my_channel.unsubscribe(subscriber_second)