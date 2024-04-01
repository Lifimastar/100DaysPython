# Average Height

# lista de alturas
student_heights = input('Input a list of student heights ').split()

# variable para guardar la suma y el numero de elementos (para no usar len())
total = 0
n_heighs = 0

# guardamos cada altura y cada una la volvemos un int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n] # suma de cada elemento en la lista
    n_heighs += 1 # numero de elementos 

average = total / n_heighs # promedio

print(round(average))


'''
total_heght = 0
for height in student_heights:
    total_heght += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = round(total_heght / number_of_students)
print(average_height)
'''