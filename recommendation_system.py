# main.py
from customer import Customer
from product import Product
from recommendation_system import RecommendationSystem
from customer_data_handler import CustomerDataHandler

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
def filter_products(products, condition):
    # Using list comprehension to filter products based on a condition (availability)
    return [product for product in products if product.is_available() == condition]

product_list = [phone, phone_case, headphones, laptop, mouse]
available_products = filter_products(product_list, True)
print(f"Available Products: {[product.get_name() for product in available_products]}")
