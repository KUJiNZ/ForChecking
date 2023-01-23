class ShoppingCart:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def get_items(self):
        return self.items

    def add(self, item):
        if self.size() == self.max_size:
            raise OverflowError('Cannot add more items.')
        else:
            self.items.append(item)

    def size(self):
        return len(self.items)

    def get_total_price(self, price_dict):
        total_price=0
        for item in self.items:
            total_price += price_dict.get(item)
        return total_price