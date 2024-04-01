# Highest Score Exercise

student_scores = input('Input a list of student scores ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max = student_scores[0]

for score in student_scores[1:]:
    if max <= score:
        max = score 

print(f'The highest score in the class is: {max}')


# Otra forma de resolverlo
'''
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)
print(f'The highest score in the class is: {highest_score}')
'''
