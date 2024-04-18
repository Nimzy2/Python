def main():
    number = int(input("Enter number: "))
    for i in range(2,number):
        if number % i == 0:
            print("Number is not a prime number")
            break
    else:
        print("number is a prime number")


if __name__ == "__main__":
    main()
