name = input("Username: ")

if len(name) >= 12 or not name.isalpha():
    print(f"{name} is not accepted username")
else:
    print(f"Welcome {name}")
