def main():
    print("This is a simple calculator.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nEnter the first number: ")
        if first_number == 'q':
            break
        second_number = input("Enter the second number: ")
        if second_number == 'q':
            break
        operator = input("Enter the operator: ")
        if operator == 'q':
            break
        if operator == '+':
            print(int(first_number) + int(second_number))
        elif operator == '-':
            print(int(first_number) - int(second_number))
        elif operator == '*':
            print(int(first_number) * int(second_number))
        elif operator == '/':
            print(int(first_number) / int(second_number))
        else:
            print("You have not entered a valid operator.")


if __name__ == '__main__':
    main()
    