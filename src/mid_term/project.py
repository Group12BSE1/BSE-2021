# repeatedly getting customer code
while True:
    code= input("Enter customer code:")
    if code == "r" or code == "c" or code == "i" :
# reading1 is the beginning meter reading
# reading2 is the final meter reading
        reading1 = input("Enter the beginning meter reading:")
        reading2 = input("Enter the final meter reading:")
        break
# reading2 has to be greater than reading1 inorder to get a positive integer
final = int(reading2)
init = int(reading1)
#init is the beginning meter reading
# we shall use final to represent the final meter reading
if final < init:
    gallons_used = (final - init )/10

elif init > final: # calculating the volume of water used
    new_gallons = (1000000000 - init)
    gallons_used = (new_gallons + final) / 10
    print("Gallons of water used:", gallons_used)
 #calculating the amount of money used
 #for residential customer
    total_money = int(total_money)
    money_per_gallon = int(money_per_gallon)
    if code == "r":
            money_per_gallon = (gallons_used * 0.0005)
            total_money = (money_per_gallon + 5.00)

    elif code == "c" and gallons_used <= 4000000:
            money_per_gallon = (gallons_used * 0.00025)
            total_money = (money_per_gallon + 1000.00)

    elif code == "i" and gallons_used <= 4000000:
            total_money = 1000.00

    elif code == "i" and gallons_used <= 10000000:
           total_money = 2000.00

    elif code == "i" and gallons_used > 10000000:
            money_per_gallon = (gallons_used * 0.00025)
            total_money = (money_per_gallon + 2000.00)

            amount_billed = round(total_money, 2)
    print("\n")
    print("Customer code:",code)
    print("Beginning meter reading:", initial_reading)
    print("Ending meter reading:", final_reading)
    print("Gallons of water used:", gallons_used)
    print("Amount billed:$", amount_billed, "\n")



