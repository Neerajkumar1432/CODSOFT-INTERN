#Task 2--Calculator 

def add(x, y): # function for addition 
    return x + y

def subtract(x, y):# function for substraction
    return x - y

def multiply(x, y): #function for multiplication
    return x * y

def divide(x, y):   #   function for division
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"The result of {num1} + {num2} is {add(num1, num2)}")
                
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
                
            elif choice == '4':
                print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
                
        else:
            print("Invalid choice. Please select a valid operation.")
    
if __name__ == "__main__":
    main()
