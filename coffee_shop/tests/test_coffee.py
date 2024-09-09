import pytest
from coffee import Coffee
from order import Order
from customer import Customer

def test_invalid_coffee_name():
    # Testing invalid coffee name (too short)
    with pytest.raises(ValueError):
        Coffee("Ro")  # Coffee name must be at least 3 characters

def test_coffee_order_count():
    # Creating a coffee instance with a valid name
    coffee = Coffee("Robusta")
    # Checking the initial number of orders
    assert coffee.num_orders() == 0  # Should be 0 since no orders have been made

    # Creating a customer instance with a valid name
    customer = Customer("Eric")
    # Creating an order for the customer
    customer.create_order(coffee, 3.5)  # Customer orders an Espresso for $3.5
    # Checking the number of orders again
    assert coffee.num_orders() == 1  # Should now be 1

def test_coffee_average_order_price():
    # Creating a coffee instance
    coffee = Coffee("Robusta")
    # Initially, there are no orders, so the average price should be 0
    assert coffee.average_price() == 0

    # Creating a customer instance
    customer = Customer("Eric")
    # Creating multiple orders for the same coffee
    customer.create_order(coffee, 4.5) 
    # First order lets say for $4.5
    customer.create_order(coffee, 5.5)
    # then Second order for $5.5  
    # Calculating and checking the average price of the orders
    assert coffee.average_price() == 5.0  
    # Average of 4.5 and 5.5 should be 5.0
