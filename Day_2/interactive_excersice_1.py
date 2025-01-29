#BMI Calculator
weight = float(input("What is your weight(in kg)? \n"))
height = float(input("What is your height(in m)? \n"))

BMI = weight/pow(height,2)
print(int(BMI))
