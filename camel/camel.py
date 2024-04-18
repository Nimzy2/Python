def main():
    # get user input
    camel_case = input("camelCase: ")
    # print snake_case
    print("Snake_case: ", end="")
    # loop through every letter
    for i in camel_case:
        # check if leter is upper case
        if i.isupper():
            # print underscores and the letter in lowercase
            print("_" + i.lower(), end="")
            # otherwise print i
        else:
            print(i, end="")
            
if __name__ == "__main__":
        main()
            