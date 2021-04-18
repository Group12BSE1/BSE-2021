# Compound interest using function

def compoundinterest(C, r, n, t):
    p = (C * (1 + r / n) ** t * n)
    return p


C = float(input("Enter initial investment:"))
r = float(input("Enter the yearly interest rate:"))
n= float(input("Enter the number of times the interest is compounded:"))
t= float(input("Enter the number of years until maturation:"))
# call the function
p= (C * (1 + r / n) ** t * n)
print("Compound interest:{}". format(p))
