from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        # Validating if the customer is a valid Customer instance
        if not isinstance(customer, Customer):
            raise ValueError("Invalid Customer.")
        # Validating if the coffee is a valid Coffee instance
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid Coffee.")
        # Validating the price is within the acceptable range
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        # Assigning the attributes
        self.customer = customer
        self.coffee = coffee
        self.price = price

        # Adding this order to both coffee's and customer's order lists
        coffee.orders.append(self)
        customer.orders.append(self)

    def __repr__(self):
        # Returning Customer's Name, Coffee's Name and Price
        return (
            f"Order("
            f"customer={self.customer.name}, "
            f"coffee={self.coffee.name}, "
            f"price={self.price})"
        )
