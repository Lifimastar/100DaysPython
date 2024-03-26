# Who's Paying Exercise

import random

# Pedimos las personas y la separamos por coma
names_string = input("Give me everybody's names, separated by a coma. ")
names = names_string.split(',')

# Otra forma con choice()
# choice = random.choice(names)

# no podemos usar la funcion choice() en este ejercicio.
# index de la lista aleatoria
choice = random.randint(0,len(names) - 1) # porque el ultimo no se incluye

# imprime el restultado
print(f'{names[choice].capitalize()} is going to buy the meal today!')
# print(f'{choice.capitalize()} is going to buy the meal today!')



