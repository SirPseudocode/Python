weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K/L): ")

if unit == 'K':
    print(f"Your weight is {round(weight * 2.205,3)} Lbs.")
elif unit == 'L':
    print(f"Your weight is {round(weight / 2.205,3)} Kgs.")
else:
    print(f"{unit} is invalid unit")