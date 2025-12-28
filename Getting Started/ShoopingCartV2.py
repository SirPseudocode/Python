foods = []
quantities = []
total = 0

while True:
    food = input("Enter a food to buq (q to quit): ")
    if food.lower() == 'q':
        break
    foods.append(food)

    p = float(input(f"Enter the price of a {food}: $"))

    q = int(input(f"Enter the quantity of {food} that you will buy: "))
    quantities.append(q)

    total += p * q
print("----- YOUR CART -----")

for food, quantity in zip(foods, quantities):
    if(food == foods[len(foods) - 1]):
        print(f"{quantity}x {food}")
        break

    print(f"{quantity}x {food}", end=' ')

print(f"Your total is: ${total:.2f}", end = '')