name1 = input("Enter the first name : \n ").upper()
name2 = input("Enter the second name : \n").upper()

name3 = name1 + name2
t =  name3.count("T")
r =  name3.count("R")
u =  name3.count("U")
e =  name3.count("E")
l =  name3.count("L")
o =  name3.count("O")
v =  name3.count("V")
print(f"T is {t} times")
print(f"R is {r} times")
print(f"U is {u} times")
print(f"E is {e} times")
print(f"L is {l} times")
print(f"O is {o} times")
print(f"V is {v} times")

true =str( t + r + u + e)
love = str(l + o + v + e)

score =int(true + love)
if 10< score or score > 90:
    print(f"Your score is {score}, you go together like coke and mentors.")
elif 40 < score < 50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

#score = int(print(f"{true}{love}"))