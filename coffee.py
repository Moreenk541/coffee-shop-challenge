from order import Order
class Coffee:
    def __init__(self,name):
        if isinstance(name,str) and  len(name) >=3:
            self._name = name
        else:
            raise ValueError("Name should have at least 3 valus")



    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,vale):
        raise AttributeError("Name is immutable") 


    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)
