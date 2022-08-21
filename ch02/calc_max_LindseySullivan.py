"""Find the maximum of three values."""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

maximum = number1

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

print('Maximum value is', maximum)