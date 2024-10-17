# customer_data_handler.py
import json

class CustomerDataHandler:
    @staticmethod
    def save_customer_data(customer):
        # Save customer data as a JSON file
        with open(f'{customer.name}_data.json', 'w') as file:
            json.dump(customer.get_purchase_history(), file)

    @staticmethod
    def load_customer_data(customer_name):
        try:
            with open(f'{customer_name}_data.json', 'r') as file:
                purchase_history = json.load(file)
                return purchase_history
        except FileNotFoundError:
            return []
