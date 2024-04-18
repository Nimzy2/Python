def main():
    # input
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    # compute
    total = difference(number_1, number_2)
    # output
    print(f"Total: {total}")


def difference(number_1, number_2):
   total= number_1 - number_2
   return total


if __name__ == "__main__":
   main()
   
