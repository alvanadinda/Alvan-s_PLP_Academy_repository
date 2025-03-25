ef calculate():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator [+,-,*,/]: ")
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                print(f"Result: {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1 * num2}")
            elif operator == "/":
                if num2 == 0:
                    print("Can't divide by zero")
                else:
                    print(f"Result: {num1 / num2}")
            else:
                print("Enter the correct operator")
        except ValueError:
            print("Enter a valid number")

        # Ask if the user wants to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again == 'no':
            break
        

calculate()