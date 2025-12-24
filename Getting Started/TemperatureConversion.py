unit = input("Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C':
    print(f"{round(temp * 9 / 5 + 32, 1)} F")
elif unit == 'F':
    print(f"{round((temp - 32) * 5 / 9, 1)} C")
else:
    print(f"{unit} is invalid unit")