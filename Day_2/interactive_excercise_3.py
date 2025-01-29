#Create a program using maths and f-string that tells us how many day,weeks,moths we have left if we live until 90 years old.

age = int(input("What is your current age? : "))

left_age = 90 - age
day = 365 * left_age
weeks = 52 * left_age
months = 12 * left_age

print(f"You have {day} days, {weeks} weeks, and {months} months left.")

