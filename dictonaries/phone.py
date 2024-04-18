def main():
    for i in range(5):
        name = input("Name: ")
        number = input("Phone Number: ")
        with open("names.csv", "a") as file:
            file.write(f"{name},{number} \n")


if __name__ == "__main__":
    main()