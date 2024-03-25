print("Welcome to the tipo calculator.")
a = float(input("What was the total bill? $"))
b = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
c = int(input("How many people to split the bill? "))

d = (a * b) / 100
e = a + d
total = e / c

print(f"Each person should pay: ${round(total, 2)}")