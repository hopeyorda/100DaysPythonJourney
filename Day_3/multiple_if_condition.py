#Multiple if condition example
print("---Welcome to the Rollercoaster!---")
height =int( input("What is your height in cm? \n"))
bill =0
if height >= 120 :
    print("You can ride rollercoaster! ")
    age = int(input("How old are you? \n"))
    if age < 12 :
        bill = 5
        print(" Child tickets are $5.")
    elif 12 < age <= 18:
        bill = 7
        print("Young tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
want_photo=input("Do you want to take photo? (Y or N) : ")
if want_photo == "Y":
    bill += 3
    print(f"Your are final bill is ${bill}")
else :
    print("Sorry, you have to grow before you can ride.")