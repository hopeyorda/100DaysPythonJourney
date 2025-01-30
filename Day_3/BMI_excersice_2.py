weight = float(input("What is your weight? \n"))
height = float(input("what is your height? \n"))

bmi = round(weight / height ** 2)
if bmi < 18.5 :
    print(f"Your BMI is {bmi}")
    print("Your are Underweight Bro. Eat much food!")
elif  bmi < 25 :
    print(f"Your BMI is {bmi}")
    print("You are are at Normal state. Keep shinning bro!")
elif  bmi < 30 :
    print(f"Your BMI is {bmi}")
    print("You are slightly overweight. So bro look at your self!")
elif   bmi < 35 :
    print(f"Your BMI is {bmi}")
    print("Your are obese.Make exercise.")
else :
    print(f"Your BMI is {bmi}")
    print("You are clinically obese. Bro you are on risk.")