# Creați fișierul Python product.py și implementați următoarelor cerințe:
# Clasa Product:
# Conține atributele: name, price și quantity.
# Metoda pentru afișarea informațiilor despre produs.
# Metoda pentru actualizarea cantității de produse.



class Product():
    def __init__(self,name,price,quantity):
        self._name = name
        self.__price = price
        self.__quantity = quantity
    
    def __str__(self):
        return f'Name : {self._name}  Price : {self.__price}  Quantity : {self.__quantity} '
    
    def display_info(self):
        print(self.__str__())
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str) and len(new_name) > 3:
            self._name = new_name
        else:
            raise ValueError("The name must be a string longer than 3 characters")
        return self._name
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self,new_quantity):
        if isinstance(new_quantity,int) and 0 < new_quantity :
            self.__quantity = new_quantity
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,new_price):
        if isinstance(new_price,(int,float)) and new_price > 0 :
            self.__price = new_price
        