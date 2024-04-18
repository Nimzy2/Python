def main():
    x = int(input("Enter number: "))
    y = square(x)
    print(y)


def square(x):
    z = x **2
    return z


if __name__ == "__main__":
    main()
    