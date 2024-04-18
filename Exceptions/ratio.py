import sys


def main():
    while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            result = number_1 / number_2
        except ZeroDivisionError:
            print("Invalid input. Number 2 can not be 0. Please try again or enter ctrl z to exit.")
        except ValueError:
            print("Invalid input. The inputs must be numbers. Please try again or enter ctrl z to exit.")
        except EOFError:
            sys.exit()
        else:
            print(f"The ratio of {number_1} and {number_2} is {result:.2f}")
            break
            

if __name__ == "__main__":
    main()