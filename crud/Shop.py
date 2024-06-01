class Shop:
    def __init__(self):
        self.products = {}
        
    def __str__(self):
        result = ""
        for category, items in self.products.items():
            result += f"-Category: {category}\n"
            for product, quantity in items:
                product_str = str(product)
                result += f"--Product [ {product_str:<10} - Qty: {quantity:<3} ]\n"
        return result
    
    def add_product(self, product, quantity):
        category_name = product.category.name
        if category_name not in self.products:
            self.products[category_name] = []
        self.products[category_name].append((product, quantity))
        
class Product:
    def __init__(self, name, price, desc, category) -> None:
        self.name = name
        self.price = price
        self.desc = desc
        self.category = category
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Price: {self.price}"
    
class Category:
    def __init__(self, name) -> None:
        self.name = name

    
shop = Shop()

phone = Category("Phone")
laptop = Category("Laptop")

product1 = Product("Smartphone LG", 699,  phone)
product2 = Product("Gaming laptop", 999, laptop)

shop.add_product(phone, 10)
shop.add_product(laptop, 5)

print(shop)