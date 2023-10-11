class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            print("Invalid product. Please provide a valid Product instance.")

    def buy_product(self, product_name, quantity=1):
        for product in self.products:
            if product.name == product_name and product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Congratulations! You have successfully bought {quantity} {product_name}(s).")
                return
        print(f"Sorry, {product_name} is not available in the desired quantity.")


shop = Shop()

# Adding products to the shop
product1 = Product("Widget", 10, 20)
product2 = Product("Gadget", 15, 15)
shop.add_product(product1)
shop.add_product(product2)

# Buying products
shop.buy_product("Widget", 5)  # Successful purchase
shop.buy_product("Gadget", 5)  # Unsuccessful purchase
