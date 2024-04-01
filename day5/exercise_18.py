# Adding Evens

'''Program that calculates the sum of all the even numbers from 1 to 100.
The first even number would be 2 and the last one is 100'''

even_sum = 0
for n in range(2, 101, 2):
    even_sum += n
print(even_sum)

# or

# alternative_sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         print(number)
#     alternative_sum += number
# print(alternative_sum)