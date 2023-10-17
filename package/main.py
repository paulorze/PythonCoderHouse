from userModel import Client, Admin

user1 = Client("paulo", "Paulo123", "Paulo", "Rzeszut", "paulo@paulo.com", "Industria 5100")
user2 = Client("agus", "Agus1234", "Agus", "Rzeszut", "agus@agus.com", "Industria 2100")
user3 = Client("leila", "Lei12345", "Leila", "Rzeszut", "leila@leila.com", "Industria 3100")
user4 = Admin("admin", "Admin1234", "Admin", "Admin", "admin@admin.com", "Calle Admin")

print(user1)
print(user2)
print(user3)
print(user4)

user1.show_cart()
user1.add_product("chocolate", 5)
user1.add_product("frutillas", 20)
user1.add_product("dulce de leche", 2)
user1.show_cart()
user1.delete_product("frutillas")
user1.show_cart()
user1.clean_cart()
user4.get_users_list()
