# Display the powers of 2 using anonymous function

num = int(input("Enter Number: "))

#terms = 10

# Uncomment code below to take input from the user
terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: num ** x, range(terms)))


print("The total terms are:",terms)
for i in range(terms):
   print(num," raised to power",i,"is",result[i]
   )