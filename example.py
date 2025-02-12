# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Computer", 900)
product4 = Product("TV", 1500)

# Имя клиента и заказ
customer1 = Customer("Mike")
customer2 = Customer("Jakson")
customer3 = Customer("Dilmurad")
customer4 = Customer("Dimash")

customer1.add_order(product1.name)
customer2.add_order(product2.name)
customer3.add_order(product3.name)
customer4.add_order(product4.name)

# Рассчитываем цену с учетом скидки
discounted_price = Order.calculate_discounted_price(product1.price, 10)
print(f"Сниженная цена на {product1.name}: {discounted_price}")  # Вывод: Сниженная цена на Laptop: 900.0
discounted_price = Order.calculate_discounted_price(product2.price, 15)
print(f"Сниженная цена на {product2.name}: {discounted_price}")
discounted_price = Order.calculate_discounted_price(product3.price, 5)
print(f"Сниженная цена на {product3.name}: {discounted_price}")
discounted_price = Order.calculate_discounted_price(product4.price, 20)
print(f"Сниженная цена на {product4.name}: {discounted_price}")

# Сезонные скидки и промокоды
seasonal_price = Discount.apply_seasonal_discount(product1.price, 20)
print(f"Сезонная скидка летом {product1.name}: {seasonal_price}")
seasonal_price = Discount.apply_seasonal_discount(product2.price, 20)
print(f"Сезонная скидка летом {product2.name}: {seasonal_price}")

promo_price = Discount.apply_promo_code(product1.price, 10)
print(f"Промо код {product1.name}: {promo_price}")
promo_price = Discount.apply_promo_code(product2.price, 10)
print(f"Промо код {product2.name}: {promo_price}")

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product1])
order3 = Order([product3, product1])
order4 = Order([product2, product4])
 
my_order = Order([product1, product2, product3, product4])

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Вывод: Всего заказов: 2
print(f"Общая цена заказов: {my_order.total_price()}")

print(customer1)
print(customer2)
print(customer3)
print(customer4)

# Выводим информацию о заказах
print(order1)  # Вывод: Заказ (Общая цена = 1000)
print(order2)  # Вывод: Заказ (Общая цена = 1500)
print(order3)
print(order4)
"""
Создание продуктов:

    product1 создается с названием "Laptop" и ценой 1000.
    product2 создается с названием "Smartphone" и ценой 500.

Расчет цены с учетом скидки:

    Рассчитывается цена product1 с 10% скидкой. Результат: 900.0.
    print(f"Discounted price of {product1.name}: {discounted_price}") выводит: Discounted price of Laptop: 900.0.

Создание заказов:

    order1 создается с одним товаром product1.
    order2 создается с двумя товарами: product1 и product2.

Общее количество заказов:

    Order.total_orders() возвращает 2, так как были созданы два заказа.
    print(f"Total orders: {Order.total_orders()}") выводит: Total orders: 2.

Информация о заказах:

    print(order1) выводит: Order(total_price=1000), так как в order1 только один товар product1 с ценой 1000.
    print(order2) выводит: Order(total_price=1500), так как в order2 два товара: product1 и product2 с общей ценой 1500.
"""