# noinspection PyBroadException
def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = int(rate)

        if hours <= 40:
            pay = hours * rate
            print("Pay:", pay)
        else:
            full = hours * rate
            over_time = hours - 40
            otp = (over_time * rate) / 2
            pay = full + otp
            print("Pay:", pay)
    except:
        print("Hey all had gone well but you entered the wrong input, Please try again!")


hours = input("Enter hours:")
rate = input("Enter rate:")
if len(hours) > 0 and len(rate) > 0:
    computepay(hours, rate)

else:
    print("Please enter something!")
