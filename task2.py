# task2
# calculator
def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2==0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      return num1/ num2
  else:
    print("Error: Invalid operator.")
    return None
def main():
  while True:
    try:
      num1= float(input("Enter the first number: "))
      num2= float(input("Enter the second number: "))
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")
  print("\nChoose an operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  while True:
    try:
      choice = int(input("Enter your choice (1-4): "))
      if choice in range(1,5):
        operator = ["+", "-", "*", "/"][choice - 1]
        break
      else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  result = calculate (num1, num2, operator)
  if result is not None:
    print("The result is:", result)
if __name__=="__main__":
  main()





















