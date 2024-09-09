class Coffee:
    def __init__(self, name):
        # Setting the name of the coffee and initializing an empty list for orders
        self.set_name(name)
        self._orders = []  # List to track orders for this coffee

    def set_name(self, name):
        # Checking if the name has 3 or more characters
        if isinstance(name, str) and len(name) >= 3:
            self.name = name  
        else:
            # Raisibg error for invalid name
            raise ValueError("Please use 3 characters or more.")  

    @property
    def orders(self):
        # Returning the list of orders
        return self._orders  

    def add_order(self, order):
        # Ensuring the order is added only once
        if order not in self._orders:
            self._orders.append(order)

    def count_orders(self):
        # Returning the total number of orders for this specific coffee
        return len(self.orders)  

    def average_price(self):
        # If there are no orders, return 0
        if len(self.orders) == 0:  
            return 0  
        # Summing the price of all orders
        total_price = sum(order.price for order in self.orders) 
        # Calculating the average price
        return total_price / len(self.orders)  
