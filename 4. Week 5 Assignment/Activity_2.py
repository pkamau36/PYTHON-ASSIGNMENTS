from Activity_1 import Gaming_laptop, Business_laptop, Ultrabook

# They behave differently when powered on

class Gaming_laptop_power(Gaming_laptop):
    def power_on(self):
        details = self.gaming_specs()
        return f"{details} roars to life with RGB lights flashing!"
    
class Business_laptop_power(Business_laptop):
    def power_on(self):
        details = self.business_specs()
        return f"{details} powers on quietly from fingerprint authentication, ready for productivity."
    
class Ultrabook_power(Ultrabook):
    def power_on(self):
        details = self.ultrabook_specs()
        return f"{details} powers on swiftly, perfect for on-the-go use."
    
# maybe it works now?
Asus= Gaming_laptop_power("Asus", "ROG", "Intel i9", "$2500", "NVIDIA RTX 3080")
HP= Business_laptop_power("HP", "EliteBook", "Intel i7", "$1800", "Fingerprint Scanner")
Dell= Ultrabook_power("Dell", "XPS 13", "Intel i5", "$1500", "Fast Boot")

print(Asus.power_on())
print(HP.power_on())
print(Dell.power_on())