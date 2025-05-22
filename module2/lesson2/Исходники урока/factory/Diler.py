class Diler:
    def __init__(self,title_diler,age):
        self.age = age
        self.title_diler = title_diler

    def create_order(self,order):
        order.start_order()
        order.show_info()
