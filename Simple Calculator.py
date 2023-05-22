#A simple calculator for:
#Addition,subtraction, Multiplication and Division
operator = input ('Enter an operator (+ - * /):')
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print(f'{operator} is not valid')
  
 


