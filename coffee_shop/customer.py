class Customer:
    def __init__(self, name):
        # Initializing a name and an empty list for orders
        self.name = name
        self._orders = []

    @property
    def name(self):
        # Getting the name
        return self._name

    @name.setter
    def name(self, value):
        # Validating the length of the string
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Please use a name with characters between 1 & 15.")

    @property
    def orders(self):
        # Returning the list of orders
        return self._orders

    def coffees(self):
        # Returning a list of unique cofffees from the orders
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        # Importing the order
        from order import Order
        # Creating a new order
        order = Order(self, coffee, price)
        # Adding the order to the customer's orders
        self._orders.append(order)  
        # Adding the order to the coffee's order list
        coffee.add_order(order)      
        return order

    def __repr__(self):
        return f"Customer(name={self.name})"
