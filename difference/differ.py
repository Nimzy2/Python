def main():
    # input
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    # computation
    difference = compute_difference(num_1, num_2)
    # output
    print(f"Total: {difference}")


def compute_difference(num_1, num_2):
    difference= num_1 - num_2
    return difference


if __name__ == "__main__":
    main()