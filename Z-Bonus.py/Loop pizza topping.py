# As the user enters each pizza topping, create a loop that prompts them to do so until they provide a value that says "quit."
# Put that ingredient on their pizza and print a message saying so

# Start a pizza toppings loop
print("The pizza topping comes next. Press 'finish' to put the session to an end.")

while True:
  topping = input("Add the toppings:").strip().lower()

  if topping == 'quit':
    print("Thank you for your purchase! preparing your topping...")
    break
  else:
      print(f"will be adding {topping} to the pizza.")