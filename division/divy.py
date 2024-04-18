def main():
    # input
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    # compute
    division = compute_division(number_1, number_2)
    # output
    print(f"Division {division}")


def compute_division(number_1, number_2):
    division= number_1 / number_2
    return division


if __name__ == "__main__":
    main()
