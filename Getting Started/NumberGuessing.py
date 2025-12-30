import random

ans = random.randint(1, 100)

temp = True

while temp:
    guess = input("Quess 1 to 100 (q to quit): ").lower()
    if guess == "q":
        print(f"The answer is {ans}")
        temp = False
    elif guess.isalnum() == False:
        print(f"{guess} is Invalid Answer")
    elif int(guess) == ans:
        print("CORRECT!!!")
        temp = False
    else:
        print(f"{guess} is incorrect")