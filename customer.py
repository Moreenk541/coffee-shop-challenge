class Customer:
    def __init__(self,name):
        
        self.name = name

    @property
    def name(self):
        return self._name  
    @name.setter
    def name(self,value) :
        if isinstance(value, str) and 1<= len(value ) <= 15 :
            self._name =value