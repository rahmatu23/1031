# main.py
import calculator

# Prompt user to enter numbers
number_1 = float(input("Enter your first number: "))
number_2 = float(input ("Enter your second number: "))

# Perform the addition operation
result1 = calculator.add(number_1, number_2)

# Display the result
print (f"{number_1} + {number_2} = {result1}")
    
# Perform the subtraction operation
result2 = calculator.subtract(number_1, number_2)

# Display the result
print (f"{number_1} - {number_2} = {result2}")

# Perform the multiplication operation
result3 = calculator.multiply(number_1, number_2)

# Display the result
print (f"{number_1} * {number_2} = {result2}")

# Perform the addition operation
result1 = calculator.add(number_1, number_2)

# Display the result
print (f"{number_1} / {number_2} = {result2}")


