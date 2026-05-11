class Product():
    def details(self):
        print("Product Details:")
class ElectronicProduct(Product):
    def electronic(self):
        print("This is an Electronic Device")
        
class MobilePhone(ElectronicProduct):
    def mobile(self):
        print("Mobile brand: Iphone \ncost:130000 \nRAM:12GB \nStorage:128GB")

p=MobilePhone()
p.details()
p.electronic()
p.mobile()

    
