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
        # Validating the Length of thhe String
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Please use a Name with characters between 1 & 15.")

    def orders(self):
        # Returning the list of orders
        return self._orders

    def coffees(self):
        # Returning a list of unique coffees from the orders
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        # Importing the order
        from order import Order
        # Creating a new order 
        order = Order(self, coffee, price)
        # Adding it to the customer's orders list
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        # Determining which customer has spent the most on a specific coffee
        max_customer = None
        max_spent = 0
        # Looping through all customers who have ordered the coffee
        for customer in {order.customer for order in coffee.orders()}:
            # Calculate total amount spent on the coffee by this specific customer
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            # Updating max if this specific customer spents more
            if total_spent > max_spent:
                max_customer = customer
                max_spent = total_spent
        return max_customer

    def __repr__(self):
        return f"Customer(name={self.name})"
