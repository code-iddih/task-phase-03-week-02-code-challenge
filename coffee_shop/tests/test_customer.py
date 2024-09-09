import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    # Testing to ensure that customer name cannot be empty
    with pytest.raises(ValueError):
        Customer("")  

    # Testing to ensure that customer name cannot exceed 15 characters
    with pytest.raises(ValueError):
        Customer("ThisNameIsTooLong")  

def test_customer_order_creation():
    # Creating a valid customer
    customer = Customer("Roberta") 
    # Using a specific coffee type for the order
    coffee = Coffee("Robusta")  
    # Creating an order with valid price
    order = customer.create_order(coffee, 5.5)  

    # Checking if the created order is in the customer's orders
    assert order in customer.orders()
    # It should contain the created order
    
    # Checking if the cofffee ordered is included in the customer's coffees
    assert coffee in customer.coffees()  
    # It should contain the coffee ordered
