# Boudreaux & Thibodeaux's Po-Boy Shop Program

menu = {
    1: ("Catfish Poboy", 14.95),
    2: ("Roast Beef Poboy", 12.95),
    3: ("Sausage Poboy", 12.95),
    4: ("Gumbo", 4.95)
    }
TAX_RATE = 0.0945

print("Boudreaux & Thibodeaux's Po-Boy Shop\n")

for number, (item, price) in menu.items():
    print(f"{number}. {item}: ${price:.2f}")

choice = int(input("\nWhat would you like to order? Type the approptiate number of the menu item: "))

if choice in menu:
        item_name, item_price = menu[choice]
        total = item_price + (item_price * TAX_RATE)
        print(f"Your total is ${total:.2f}")
else:
    print("Invalid selection . Please restart the program and choose a valid menu item.")
