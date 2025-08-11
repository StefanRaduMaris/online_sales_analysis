# Creați fișierul Python product_manager.py și implementați următoarele cerințe:
# Clasa ProductManager:
# Conține ca atribut o listă cu toate produsele disponibile.
# Adăugarea de produse.
# Afișarea tuturor produselor.
# Afișarea valorii totale a tuturor produselor.

from Product import *

class ProductManager(Product):
    def __init__(self):
        self.products = []
    
    def __str__(self):
        return f'Produs : {self.products}'

    def add_product(self,product):
        if not product in self.products:
            self.products.append(product)
    
    def display_info(self):
        for product in self.products:
            print(product)
    
    def total(self):
        return sum(product.price*product.quantity for product in self.products)
    
    def remove(self,our_name):
        for product in self.products:
            if product.name == our_name:
                self.products.remove(product) 