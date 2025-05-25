class Body:

    def __init__(self, body_type, color):
        self.body_type = body_type
        self.color = color

    def __str__(self):
        return f"{self.color.title()} {self.body_type}"
