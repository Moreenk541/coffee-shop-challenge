class Order:
    def __init__(self,customer, coffee, price):
    
        from customer import Customer
        from coffee import Coffee



        if not isinstance(customer,Customer):
            return TypeError("")

        if not isinstance(coffee,Coffee):
            raise TypeError("")
        
        if not isinstance(price, float ) and 1.0 <= 10.0:
            raise TypeError("")
        
        self.customer =customer
        self.coffee = coffee
        self.price = price


    @property
    def coffee(self):
       return self._coffee
    
    @property
    def customer(self):
       return self._customer


    @property
    def price(self):
       return self._price  


        
       