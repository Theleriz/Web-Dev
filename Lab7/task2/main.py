from models import Laptop, Smartphone

def test():
    macbook = Laptop("Apple", "MacBook Pro", 2000, 16, 512)
    pixel = Smartphone("Google", "Pixel 8", 799, 100)

    inventory = [macbook, pixel]

    for item in inventory:
        print(item)
    
        print(f"Display Name: {item.get_description()}")
        print("-------")

    macbook.upgrade_ram(16)
    macbook.extend_storage(256)
    print(pixel.check_battery())

    new_price = pixel.apply_discount(10)
    print(f"Pixel 8 new price after discount: ${new_price}")
    print(pixel.check_battery())
    pixel.repair_smartphoe()
    
if __name__ == "__main__":
    test()