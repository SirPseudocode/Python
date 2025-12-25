name = input("Username: ")

if len(name) >= 12 or name.find(" ") != -1 or name.isdigit():
    print(f"{name} is not accepted username")
else:
    print(f"Welcome {name}")
