# Python Program to find the factors of a number

# This function computes the factor of the argument passed
from tkinter.tix import INTEGER


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

#num = 320
num = int(input("Enter Number: "))
print_factors(num)