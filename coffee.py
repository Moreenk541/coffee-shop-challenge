from order import Order
class Coffee:
    def __init__(self,name):
        if isinstance(name,str) and 1<= len(name)<=15:
            self._name = name



    @property
    def name(self):
        return self._name
    @name.setter
    def name(self):
        return "immutable value"  


    def Order(self):
        return(order for order in Order.all if order.coffee == self)
    
    def customers(self):
        return list({order.customer for order in self.orders()})
          