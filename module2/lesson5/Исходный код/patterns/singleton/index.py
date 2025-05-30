class ORM:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
class ORMImpl(ORM):
    def __init__(self):
        super().__init__()
# ORMImpl()

#     def insert(self):
#         pass
#
#     def delete(self):
#         pass
#
#     def update(self):
#         pass
#
#     def select(self):
#         pass
# obj1 = ORM()
# obj2 = ORM()
# print(obj1 is obj2)
#
#
# class Catalog:
#     def __init__(self):
#         self.orm = ORM()
#
#     def show_items(self):
#         self.orm.select()
#     def remove_items(self):
#         self.orm.delete()