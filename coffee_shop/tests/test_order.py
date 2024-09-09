import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    # Creating a customer instance 
    customer = Customer("Eric")  
    # Creating a coffee instance for testing
    coffee = Coffee("Robusta")  
    
    # Initializing a new order with the customer, coffee, and a price
    order = Order(customer, coffee, 4.5)  
    
    # Verifyingg that the order is correctly associated with the customer
    assert order.customer == customer  
    # It should match the initialized customer
    
    # Verifying that the order is correctly associated with the coffee
    assert order.coffee == coffee  
    # It should match the initialized coffee
    
    # Verifying that the order price is correctly set
    assert order.price == 4.5  
    # It should match the initialized price

def test_order_price_validation():
    # Creating a customer instance for testing
    customer = Customer("Eric")  
    # Creating a coffee instance 
    coffee = Coffee("Robusta")  
    
    # Testing to ensure that the order price cannot be less than 1.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  
        # It should return  - Invalid price - less than minimum
    
    # Testing to ensure that the order price cannot exceed 10.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 12.0)  
        # It should return - Invalid price - exceeds maximum
