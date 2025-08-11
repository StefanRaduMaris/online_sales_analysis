# Clasa Cart:
# Atribut: cart_items – lista de produse din coș.
# Metode:
# Adăugarea produselor în coș.
# Calcularea valorii totale a coșului, adică a sumei de plată.
# Afișarea conţinutul coşului.

from Product import *

class Cart():
    def __init__(self):
        self.cart_items =[]

    def add_item_in_cart(self,product):
        for prod in self.cart_items:
            if prod.name == product.name :
                prod.quantity += 1
                break
        else :
                self.cart_items.append(Product(product.name,product.price,1))

    def total_cart(self):
        return f'Total price is :{sum(product.price *product.quantity for product in self.cart_items)} Ron'
    
    def __str__(self):
        if not self.cart_items:
            return "Coșul este gol."
        result = "Produsele din coș:\n"
        for produs in self.cart_items:
            result += f"- {produs.name}: Quantity {produs.quantity}, Price {produs.price} RON\n"
        return result
    
    def display_info(self):
        print(self.__str__())

    
