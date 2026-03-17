class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_description(self):
        return f"{self.brand} {self.model}"

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        return self.price

    def __str__(self):
        return f"Device: {self.brand} {self.model}, Price: ${self.price:.2f}"


class Laptop(Device):
    def __init__(self, brand, model, price, ram_gb, storage_gb):
        super().__init__(brand, model, price)
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

    def upgrade_ram(self, additional_gb):
        self.ram_gb += additional_gb
        print(f"RAM upgraded to {self.ram_gb}GB")

    def extend_storage(self, additional_storage):
        self.storage_gb += additional_storage
        print(f"Storage extended to {self.extend_storage}")

    def get_description(self):
        return f"Laptop: {self.brand} {self.model} ({self.ram_gb}GB RAM) ({self.storage_gb}GB storage)"


class Smartphone(Device):
    def __init__(self, brand, model, price, battery_health):
        super().__init__(brand, model, price)
        self.battery_health = battery_health

    def check_battery(self):
        return f"Battery Health: {self.battery_health}%"
    
    def repair_smartphoe(self):
        if(self.battery_health <= 79):
            print("We change the battery to new battery")
            self.battery_health = 100
            print(f"Now {self.model} has batttery health {self.battery_health}")
        else:
            print(f"{self.battery_health} is okay for daily tasks")

    def get_description(self):
        return f"Smartphone: {self.brand} {self.model} - Battery at {self.battery_health}%"