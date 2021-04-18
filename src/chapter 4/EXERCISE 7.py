# noinspection PyBroadException
def computegrade(score):
    try:
        score = float(input("Enter the score"))
        if score >= 0.9:
            print("Grade A")
        elif score >= 0.8:
            print("Grade B")
        elif score >= 0.7:
            print("Grade C")
        elif score >= 0.6:
            print("Grade D")
        elif score < 0.6:
            print("Grade F")
        else:
            print("Bad score")
    except:
        print("please revise ur values")


score = float(input("Enter the score:"))
if score >= 1.1:
    computegrade(score)

else:
    print("Enter correct numeric values")
