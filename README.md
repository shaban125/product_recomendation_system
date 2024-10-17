---

# **E-commerce Recommendation System**

This is a simple E-commerce Recommendation System built using Python. It recommends products to customers based on their previous purchase history using **conditional probability** and basic **object-oriented programming (OOP)** principles.

## **Features**
- **Product and Customer Classes**: Encapsulate details like product pricing, availability, and customer preferences.
- **Product Recommendation**: Recommends products based on customer purchase history.
- **File Handling**: Customer purchase data is stored and retrieved from files.
- **List Comprehension**: Efficiently filters and generates product recommendations.

## **How to Use**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shaban125/product_recomendation_system
   ```

2. **Go into the project folder**:
   ```bash
   cd ecommerce-recommendation-system
   ```

3. **Run the Python script**:
   ```bash
   python main.py
   ```

## **How It Works**

- The system recommends products based on what the customer has bought in the past.
- It uses conditional probability to calculate the likelihood of recommending related products. For example, if a customer buys a phone, there’s a 70% chance they will buy a phone case.
- The program saves customer purchase history to a file, which can be used to personalize future recommendations.

## **Example**

1. **Create a Customer**:
   ```python
   customer = Customer('Alice', ['Phone'])
   ```

2. **Get Product Recommendations**:
   ```python
   recommender = RecommendationSystem()
   recommendations = recommender.recommend_products(customer)
   print(recommendations)
   ```

## **Project Structure**

```
ecommerce-recommendation-system/
│
├── customer.py                   # Customer class
├── product.py                    # Product class
├── recommendation_system.py      # Recommendation logic
├── customer_data_handler.py      # File handling for customer data
├── main.py                       # Main script
└── README.md                     # Documentation
n
```

## **Technologies Used**
- **Python** for the core functionality.
- **File Handling** to store and load customer data.
- **OOP** principles for structuring the product and customer classes.
- **Conditional Probability** to provide product recommendations.

## **Future Improvements**
- Add more complex recommendation algorithms using machine learning.
- Create a graphical interface for easier use.
