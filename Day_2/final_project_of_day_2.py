print("---Welcome to tip calculator!---")
bill=float(input("What is the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, or 15 ?"))
percentage = percentage * bill / 100
bill = bill + percentage
num_people = float(input("How many people to split the bills? "))

each_person_pay = bill / num_people
print(f"Each person should pay : ${each_person_pay}")