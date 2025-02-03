print("---Welcome to the Rollercoaster!---")
height =int( input("What is your height in cm? \n"))

if height >= 120 :
    print("You can ride rollercoaster! ")
    age = int(input("How old are you? \n"))
    if age < 12 :
          print("Please pay $5.")
    elif 12 < age <= 18:
        print("Please pay $7")
    else:
          print("Please pay $12")
else :
    print("Sorry, you have to grow before you can ride.")