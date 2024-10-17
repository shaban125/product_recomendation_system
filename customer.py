# customer.py
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []  # List to store purchased products

    # Method to add a purchased product to history
    def add_purchase(self, product):
        self.purchase_history.append(product)

    # Method to retrieve purchase history
    def get_purchase_history(self):
        return self.purchase_history
