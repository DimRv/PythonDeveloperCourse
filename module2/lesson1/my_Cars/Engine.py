class Engine:
    def __init__(self, title, capacity, power):
        self.power = power
        self.capacity = capacity
        self.title = title

    def __str__(self):
        return f"Двигатель {self.title} объем {self.capacity} {self.power} л.с."
