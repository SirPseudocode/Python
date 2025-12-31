import random

ans = random.randint(1, 100)

while True:
    guess = input("Guess 1 to 100 (q to quit): ").lower()

    if guess == "q":
        print(f"The answer is {ans}")
        print("Goodbye!")
        break
    
    if not guess.isdigit(): 
        print(f"'{guess}' is not a valid number. Please enter a number.")
        continue

    guess_num = int(guess)

    if guess_num == ans:
        print("CORRECT!!!")
        break
    elif guess_num > ans:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")