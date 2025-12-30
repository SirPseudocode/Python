import random

ans = random.randint(1, 100)

temp = True

while temp:
    guess = input("Quess 1 to 100 (q to quit): ").lower()
    if guess == "q":
        print(f"The answer is {ans}")
        break
    if()