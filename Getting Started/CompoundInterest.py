p = r = t = 0

while p <= 0:
    p = float(input("Enter the initial amount of money: "))
    if p <= 0:
        print("The initial amount of money cannot be less than or equal zero")

while r <= 0:
    r = float(input("Enter the annual interest rate (decimal): "))
    if r <= 0:
        print("The the annual interest rate cannot be less than or equal zero")

while t <= 0:
    t = float(input("Enter the number of years: "))
    if t <= 0:
        print("The the number of years cannot be less than or equal zero")

print(f"The amount of money accumulated after {t} years, including annual interest({r})= {p * (1+r) ** t:.2f}")