#Dictionarie and Nesting
#blind auction completed project

#programing_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# }

#Retrieving items from dictionary
#print(programing_dictionary['Function'])

#Adding new items to dictionary
#programing_dictionary['Loop'] = 'The action of doing something over and over again'
#print(programing_dictionary)

#Create an empty dictionary
#empty_dictionary = {}

#Wipe an existing dictionary
#programing_dictionary = {}
#print(programing_dictionary)

#Edit an item in a dictionary
#programing_dictionary["Bug"] = 'A moth in your computer'

#print(programing_dictionary)

#Loop through a dictionary
#for key in programing_dictionary:
#     print(key) # print keys
#     print(programing_dictionary[key]) # value

'''Grading Program Exercise'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for scores in student_scores:
    if student_scores[scores] >= 91:
        student_grades[scores] = 'Outstanding'
    elif student_scores[scores] >= 81:
        student_grades[scores] = 'Exceeds Expectations'
    elif student_scores[scores] >= 71:
        student_grades[scores] = 'Acceptable'
    else:
        student_grades[scores] = 'Fail'
    
print(student_grades)
