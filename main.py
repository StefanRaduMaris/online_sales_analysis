# Creați fișierul Python main.py și în el:
# creați instanța ProductManager.
# adăugați câteva produse arbitrare.
# afișați produsele și valoarea totală a inventarului.

from product_manager import *
from Cart import *
from random import *


def main():
    our_list = ProductManager()

    our_list.add_product(Product('Masa',130,20))
    our_list.add_product(Product('Tv',4000,15))
    our_list.add_product(Product('Scaun',30,20))
    our_list.add_product(Product('Laptop',3750,15))

    # our_list.display_info()
    # print(f'Inventory total cost : {our_list.total()} Ron')
    # our_list.remove('Scaun')
    # our_list.display_info()

    customer_one = Cart()
    while len(customer_one.cart_items) < 3 :
        for i in range(0,3):
            customer_one.add_item_in_cart(choice(our_list.products))
    
    customer_one.display_info()
    print(customer_one.total_cart())



if __name__ == '__main__':
    main()
    



