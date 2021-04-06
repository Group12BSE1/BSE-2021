# City-Worker pay check Program
try:
    location = str(input("What is the location"))
    pay = int(input("what is the pay"))

    if location == "Space":
        print("Without doubt I'll take it")
    elif (location == "Kampala") and pay < 10000000:
        print("No way!")
    elif (location == "Mbarara") and pay > 4000000:
        print("Sure, I can work with this")
    elif (location == "") and pay >= 6000000:
        print("Sure, I can work with this")
except:
    if (location == "Mbarara") and pay < 4000000:
        print("No Thanks, I can find something better")
