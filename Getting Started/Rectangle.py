r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of coloumns: "))
s = input("Enter the symbol: ")

for x in range(r):
    for y in range(c):
        print(s, end='')
    print()
