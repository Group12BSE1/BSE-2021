# applying IF AND ELSEIF FUNCTIONS
x = int(input("What is your age?"))
if x >= 18:
    print("You can vote")
elif 0 < x <= 17:
    print("Too young to vote")
else:
    print("You are a time traveller")
