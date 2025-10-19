num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print("\nAddition:", add)
print("Subtraction:", sub)
print("Multiplication:", multi)
print("Division:", div)
