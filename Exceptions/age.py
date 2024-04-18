def main():
    """
    a program that only accepts age as a valid positive  integer
    """
    age = int(input("Input the age: "))
    try:
        if age < 0:
            raise ValueError("Invalid age. Age can not be negative!")
    except ValueError as e:
        print(e)
    else:
        print(f"In 20 years you will be {age + 20}")
        
    # finally:
    #     print("There may or may not be have been an exception.")

        



if __name__ == "__main__":
    main()