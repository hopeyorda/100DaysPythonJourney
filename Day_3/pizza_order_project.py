print("---Welcome to Python Pizza Deliveries!")
bill = 0
pizza_size = input("What size pizza do you want (S or M or L) : ")
if pizza_size == "S":
    bill = 15
    pepperoni = input("Do you want pepperoni? (Y or N) : ")
    if pepperoni == "Y":
        bill += 2
elif pizza_size == "M":
    bill = 20
    pepperoni = input("Do you want pepperoni? (Y or N) : ")
    if pepperoni == "Y":
        bill += 3
elif pizza_size == "L":
    bill = 25
    pepperoni = input("Do you want pepperoni? (Y or N) : ")
    if pepperoni == "Y":
        bill += 3
else:
    print("There is no pizza size like this.")
extra_cheese = input("Do you want an extra cheese? (Y or N) : ")
if extra_cheese == "Y":
    bill += 1
print(f"Total bill is : ${bill}")


