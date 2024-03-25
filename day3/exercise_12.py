# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

total1 = t + r + u + e

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e2 = name1.count('e') + name2.count('e')

total2 = l + o + v + e2

score = str(total1) + str(total2)
score_int = int(score)


if score_int < 10 or score_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")