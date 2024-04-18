def main():
    # input
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    # computation
    total = compute_total(number_1, number_2)
    # output
    print(f"Total: {total}")


def compute_total(number_1, number_2):
    """
    This function computes total of 2 numbers

    Arguments:
        number_1 (int): Any number
        number_2 (int): Any number 

    Returns:
        total (int): total of number_1 and number_2
    """
    total = number_1 + number_2
    return total


if __name__ == "__main__": 
    main()


