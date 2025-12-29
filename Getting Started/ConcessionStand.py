menu = {"pizza" : 3.00,
        "nachos" : 4.50, 
        "popcorn" : 6.00, 
        "fries" : 2.50, 
        "chips" : 1.00, 
        "pretzel" : 3.50, 
        "soda" : 3.00, 
        "lemonade" : 4.25}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key.capitalize():10} : IDR {value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if(food == 'q'):
        break

    cart.append(food)
    total += menu[food]

print("----- YOUR CART -----")
for grocery in cart:
    print(grocery.capitalize())

print(f"\nTotal = IDR {total}")