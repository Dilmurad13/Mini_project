class Discount:
    def __init__(self):
        self.description = "description" 
        self.percent = "percent"
        
    @staticmethod
    def apply_seasonal_discount(price, season):
        """
        Применяет сезонную скидку.

        Args:
            price: Исходная цена товара.
            season: Название сезона (например, "лето", "зима").

        Returns:
            Цена со скидкой, если сезонная скидка активна, иначе исходная цена.
        """
        if season == "лето":
            discount = Discount("Летняя скидка", 20)
            return Discount.calculate_discounted_price(price, discount)
        elif season == "зима":
            discount = Discount("Зимняя скидка", 10)
            return Discount.calculate_discounted_price(price, discount)
        else:
            return price

    @staticmethod
    def apply_promo_code(price, promo_code):
        """
        Применяет скидку по промокоду.

        Args:
            price: Исходная цена товара.
            promo_code: Промокод.

        Returns:
            Цена со скидкой, если промокод действителен, иначе исходная цена.
        """
        if promo_code == "SUPER_SALE":
            discount = Discount("Скидка по промокоду", 20)
            return Discount.calculate_discounted_price(price, discount)
        else:
            return price