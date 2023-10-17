#Importamos json para poder manejar los datos de los archivos.
import json
from errorModel import *

#Creamos una clase User que tendra todos los atributos y funciones comunes a todos los usuarios
class User:
    def __init__ (self, username, password, first_name, last_name, email, address):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.admin = False
        with open ('./package/users.json', 'r+', encoding='UTF-8') as users:
            users_list = json.load(users)
            users_list.append({
                "username": self.username,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "address": self.address,
                "admin": self.admin
            })
            users.seek(0)
            users.write(json.dumps(users_list, indent = 2))

    def __str__(self):
        return f"El usuario {self.username} se llama {self.first_name} {self.last_name}. Su email es {self.email} y su direccion {self.address}."

class Admin(User):
    def __init__(self, username, password, first_name, last_name, email, address):
        super().__init__(username, password, first_name, last_name, email, address)
        self.admin = True

    def get_users_list(self):
        with open ('./package/users.json', 'r', encoding='UTF-8') as users:
            users_list = json.load(users)
            print("La lista de usuarios es:")
            print(users_list)

#Creamos la clase Client, que sera la clase correspondiente a los usuarios comunes. No seran Admin y podran agregar y quitar productos de sus carritos, a la de ver su carrito correspondiente o vaciarlo
class Client (User):
    def __init__(self, username, password, first_name, last_name, email, address):
        super().__init__(username, password, first_name, last_name, email, address)
        self.admin = False
        self.cart = []

    def add_product (self, product, quantity):
        try:
            isEmpty(product)
            isNaN(quantity)
            self.cart.append({"product": product, "quantity": quantity})
            print(f"Se ha/n agregado {quantity} unidad/es del producto {product} a su carrito.")
        except NaNError as e:
            print(f"Error: {e}")
        except EmptyError as e:
            print(f"Error: {e}")
    def delete_product (self, product_to_delete):
        index = None
        for product in self.cart:
            if product['product'] == product_to_delete:
                index = self.cart.index(product)
        if index != None :
            del self.cart[index]
            print(f"El producto {product_to_delete} ha sido eliminado correctamente del carrito.")
        else:
            print(f"El producto {product_to_delete} no existe en su carrito.")
    
    def show_cart(self):
        if len(self.cart) > 0:
            print("Usted cuenta con los siguientes productos en su carrito:")
            for product in self.cart:
                print(f"Producto: {product['product']}. Cantidad: {product['quantity']}")
            print("Fin del carrito")
        else:
            print("Usted no cuenta con productos en su carrito.")

    def clean_cart(self):
        self.cart = []
        print("Su carrito se ha vaciado correctamente.")
