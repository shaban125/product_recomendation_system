import json

# Step 1: Product Class
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


# Step 1: Customer Class
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


# Step 2: Product Recommendation based on Conditional Probability
class RecommendationSystem:
    def __init__(self):
        # Example of pre-calculated conditional probabilities
        self.purchase_data = {
            ('Phone', 'Phone Case'): 0.7,
            ('Phone', 'Headphones'): 0.5,
            ('Laptop', 'Mouse'): 0.6
        }

    # Abstraction: The internal logic of recommendation is hidden
    def recommend_products(self, customer):
        recommendations = {}
        
        # Loop through customer's purchase history
        for product in customer.get_purchase_history():
            for (purchased_product, recommended_product), probability in self.purchase_data.items():
                if product == purchased_product:
                    recommendations[recommended_product] = probability

        # Sort products by probability using list comprehension
        return sorted(recommendations, key=recommendations.get, reverse=True)


# Step 3: File Handling - Save and Retrieve Customer Data
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

# Step 4: List Comprehension and Filtering
def filter_products(products, condition):
    # Using list comprehension to filter products based on a condition (availability)
    return [product for product in products if product.is_available() == condition]


# Example of Using the Classes and Methods
if __name__ == "__main__":
    # Step 1: Create Product Instances
    phone = Product("Phone", 700, True)
    phone_case = Product("Phone Case", 30, True)
    headphones = Product("Headphones", 50, True)
    laptop = Product("Laptop", 1000, True)
    mouse = Product("Mouse", 25, False)  # Unavailable product
    
    # Step 1: Create a Customer and add purchases
    customer = Customer("Samuel")
    customer.add_purchase("Phone")
    customer.add_purchase("Laptop")
    
    # Step 3: Save and Load Customer Data
    CustomerDataHandler.save_customer_data(customer)
    loaded_purchase_history = CustomerDataHandler.load_customer_data("Samuel")
    print(f"Loaded Purchase History: {loaded_purchase_history}")
    
    # Step 2: Recommend Products based on Conditional Probability
    recommendation_system = RecommendationSystem()
    recommendations = recommendation_system.recommend_products(customer)
    print(f"Recommended Products: {recommendations}")
    
    # Step 4: Filter Available Products
    product_list = [phone, phone_case, headphones, laptop, mouse]
    available_products = filter_products(product_list, True)
    print(f"Available Products: {[product.get_name() for product in available_products]}")
