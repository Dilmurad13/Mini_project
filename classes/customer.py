class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def __str__(self):
        return f"Имя: {self.name}, Заказы: {self.orders}"