# Treasure Map

# Creamos 3 listas que seran los mapas.
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Creamos una lista de listas de mapas
map = [row1, row2, row3]

# Pedimos donde quiere colocar la X en la lista 12, 1 es la fila, 2 la columna
position = input("Where do you want to put the treasure? ")

row = int(position[1])-1
col = int(position[0])-1

map[row][col] = 'X'

print(f"{row1}\n{row2}\n{row3}")

# Otra forma

# horizontal = int(position[1])-1
# vertical = int(position[0])-1

# map[vertical - 1][horizontal - 1] = 'X'

