def calculator():
 try:
    num1 = float(input('Please enter your first number: '))
    num2 = float(input('Please enter your second number: '))
    operation = input('Please enter an operation: + - * /: ')
 except ValueError as ERROR:
  print('invalid number input\nPlease try again')
  return
 if operation == '+':
  print(num1 + num2)
 elif operation == '-':
  print(num1 - num2)
 elif operation == '*':
  print(num1 * num2)
 elif operation == '/':
  try:
   print(num1 / num2)
  except ZeroDivisionError as ERROR:
   print('Invalid equation\n')
  return
 else:
  print('invalid operation')
while True:
 calculator()







