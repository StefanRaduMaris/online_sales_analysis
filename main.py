# Creați fișierul Python main.py și în el:
# creați instanța ProductManager.
# adăugați câteva produse arbitrare.
# afișați produsele și valoarea totală a inventarului.

from product_manager import *

def main():
    our_list = ProductManager()

    our_list.add_product(Product('Masa',130,20))
    our_list.add_product(Product('Tv',4000,15))
    our_list.add_product(Product('Scaun',30,20))
    our_list.add_product(Product('Laptop',3750,15))

    our_list.display_info()
    print(f'Inventory total cost : {our_list.total()} Ron')

    our_list.remove('Scaun')
    our_list.display_info()


if __name__ == '__main__':
    main()
    



