#Functions with Outputs

# def format_name(name1, name2):
#     if name1 == '' or name2 == '':
#         return "You didn't provide valid inputs."
#     formate_name1 = name1.title()
#     formate_name2 = name2.title()
#     return f'{formate_name1} {formate_name2}'

# print(format_name(input('What is your first name? '), input('What is your last name? ')))

#Days in Month Exercise

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True:
    return month_days[month-1] + 1
  else:
    return month_days[month-1]

print(days_in_month(1045, 5))
