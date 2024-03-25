# Life in Weeks Exercise

age = input("What is your current age? ")

my_days = (int(age) * 365)
days = (90 * my_days / int(age)) - my_days

weeks = (90 * 52) - (int(age) * 52)

months = (90 * 12) - (int(age) * 12)

print(f"You have {int(days)} days, {weeks} weeks and {months} months left.")


# age_as_int = int(age)

# year_remaining = 90 - age_as_int
# days_remaining = year_remaining * 365
# weeks_remaining = year_remaining * 52
# months_remainig = year_remaining * 12

# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remainig} months left.")