class Category:
    count = 0

    def __init__(self,title_cat):
        self.title_cat = title_cat
        Category.count += 1
        self.id = Category.count