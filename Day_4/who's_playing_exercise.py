import random

name =input("Give me everybody's names, separated by "
       "comma : ")
name1 = name.split(", ")
name2 = len(name1)

random_choice = random.randint(0,name2-1)

print(name1[random_choice] + " is pay the bill.f")
