# If AND ELSE
Y = int(input("Number of guests"))
if Y <= 50:
    print(" It costs $4,000")
elif 50<Y<=100:
    print("It costs $10,000")
elif 100<Y<=200:
    print("It costs $15,000")
else:
    print("It costs $20,000")