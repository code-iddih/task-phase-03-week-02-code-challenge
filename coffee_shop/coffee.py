class Coffee:
    def __init__(self, name):
        self.set_name(name)  
        self.orders = []  # List to track orders for this coffee

    def set_name(self, name):
        # Checking if the name hhas 3 or more characters
        if isinstance(name, str) and len(name) >= 3:
            self.name = name  
        else:
            raise ValueError("Please Use 3 Characters or More.")  # Raise error for invalid name

    def get_orders(self):
        # Returning the list of orders
        return self.orders  

    def get_customers(self):
        # Returning a List of Customers who Orderedd this specific of coffee
        return list({order.customer for order in self.orders})

    def count_orders(self):
        # Returning the total number of orders for this specific coffee
        return len(self.orders)  

    def average_price(self):
        # If thehre are no orders, return 0
        if len(self.orders) == 0:  
            return 0  
        # Summing the price of all orders
        total_price = sum(order.price for order in self.orders) 
        # Calculating the average price
        average = total_price / len(self.orders)  
        return average   
