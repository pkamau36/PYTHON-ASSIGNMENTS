# Parent class
class laptop:
    def __init__(self, brand, model, processor, price):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.price = price
        
    def specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Processor: {self.processor}, Price: {self.price}"
    
# Child class
class Gaming_laptop(laptop):
    def __init__(self, brand, model, processor, price, gpu):
        super().__init__(brand, model, processor, price)
        self.gpu = gpu
        
    def gaming_specs(self):
        parent_specs = super().specs()
        return f"{parent_specs}, GPU: {self.gpu}"
    
# Child class
class Business_laptop(laptop):
    def __init__(self, brand, model, processor, price, security_feature):
        super(). __init__(brand, model, processor, price)
        self.security_feature= security_feature

    def business_specs(self):
        parent_specs = super().specs()
        return f"{parent_specs}, Security Feature: {self.security_feature}"
    
# Child class
class Ultrabook(laptop):
    def __init__(self, brand, model, processor, price, speed):
        super(). __init__(brand, model, processor, price)
        self.speed= speed
    
    def ultrabook_specs(self):
        parent_specs = super().specs()
        return f"{parent_specs}, Speed: {self.speed}"
    
# Maybe it works now?
if __name__ == "__main__":
    Asus= Gaming_laptop("Asus", "ROG", "Intel i9", "$2500", "NVIDIA RTX 3080")
    HP= Business_laptop("HP", "EliteBook", "Intel i7", "$1800", "Fingerprint Scanner")
    Dell= Ultrabook("Dell", "XPS 13", "Intel i5", "$1500", "Fast Boot")


    print(Asus.specs())
    print(Asus.gaming_specs())
    print(HP.specs())
    print(HP.business_specs())
    print(Dell.specs())
    print(Dell.ultrabook_specs())

