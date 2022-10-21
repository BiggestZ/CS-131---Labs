# Zahir Choudhry
# 9/16/2021
#Lab #2 A - Quadratic Equation Debuggin

from math import sqrt

def quadratic (a,b,c):

    #calculate the quadratic formula
    root = sqrt(( b**2 )-( 4 * a * c))
    print(str(root) + " is the root\n")
    #calculate and print the first root
    numerator = (-b) + root
    print(str(str(numerator) + " is the numerator\n"))
    x = numerator / (2 * a)
    #return statement
    return x
#Input Statements    
a = int(input("Enter the coefficient for the degree two term: "))
b = int(input("\nEnter the coefficient for the degree one term: "))
c = int(input("\nEnter the coefficient for the constant: "))
#Print Statement
print("\nOne of the roots is", quadratic(a,b,c), '\n')