def main():
    while True:
        """
        a program that only admits people who are 18 years and above
        """
        age = int(input("Enter age for admission: "))
        
        try:
            if age < 18:
                raise ValueError("You need to be 18 years and above.")
        except ValueError as e:
                print(e)
        else:
            print("You are admitted")
            break


if __name__ == "__main__":
    main()
