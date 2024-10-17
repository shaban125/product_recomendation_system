# product.py
class Product:
    def __init__(self, name, price, availability):
        self.__name = name  # Encapsulating product details
        self.__price = price
        self.__availability = availability
    
    # Getter methods for product details
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def is_available(self):
        return self.__availability
