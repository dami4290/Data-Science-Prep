class Customer:
    def __init__(self, income, age, sex, country):
        self.income=income
        self.age=age
        self.sex=sex
        self.country=country
    
    def purchase(self,product):
        print("Customer from ", self.country, "purchase ", product.brand )

class Product:
    def __init__(self, price, brand, color):
        self.price=price
        self.brand=brand #string
        self.color=color






def main():
    customer1=Customer(100,36,"Male","China")
    customer2=Customer(150,27,"Female","Korea")
    product1=Product(30,"Apple", "Black")
    customer1.purchase(product1)


if __name__=="__main__":
    main()

