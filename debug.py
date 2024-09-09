from customer import Customer
from coffee import Coffee
from order import Order

def run_debug():
    # Creating a customer instance for testing
    customer1 = Customer("Eric")  
    # Creating a coffee instance for testing
    coffee1 = Coffee("Robusta")  
    
    # Creating an order for the customer and coffee with a specific price
    order1 = customer1.create_order(coffee1, 5.0)  
    
    # Printing details of the created order
    print(f"Customer Name: {order1.customer.name}, Coffee Type: {order1.coffee.name}, Price is: {order1.price}")

    # Printing the number of orders for the specified coffee
    print(f"{coffee1.name} has {coffee1.num_orders()} order(s).")
    
    # Printing the average price for the specified coffee
    print(f"The Average price for {coffee1.name} is : {coffee1.average_price()}")

if __name__ == "__main__":
    run_debug()
