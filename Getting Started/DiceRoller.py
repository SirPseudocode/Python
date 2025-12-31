import random

n = int(input("Enter number of dice: "))

dice_art = {
    1 : ("┌─────────┐", 
         "│         │", 
         "│    ●    │", 
         "│         │", 
         "└─────────┘"), 
    2 : ("┌─────────┐", 
         "│  ●      │", 
         "│         │", 
         "│      ●  │", 
         "└─────────┘"), 
    3 : ("┌─────────┐", 
         "│  ●      │", 
         "│    ●    │", 
         "│      ●  │", 
         "└─────────┘"), 
    4 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│         │", 
         "│  ●   ●  │", 
         "└─────────┘"), 
    5 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│    ●    │", 
         "│  ●   ●  │", 
         "└─────────┘"), 
    6 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "└─────────┘"), 
}

ans = []
total = 0

for x in range(n):
    temp = random.randint(1, 6)
    total += temp
    ans.append(temp)

for line_idx in range(5):
    for die_value in ans:
        print(dice_art[die_value][line_idx], end=" ")
    print()

print(f"TOTAL: {total}")