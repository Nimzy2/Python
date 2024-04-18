def main():
    camelCase = input("Enter a variable in camel case: ")
    snake_case = ""
    for i in range(len(camelCase)):
        if camelCase[i].isupper():
            if i == 0:
                snake_case += camelCase[i].lower()
            else:
               snake_case += "_" + camelCase[i].lower()
        else:
            snake_case += camelCase[i]

    # for char in camelCase:
    #     if char.isupper():
    #         snake_case += ("_" + char.lower())
    #     else:
    #         snake_case += char
            
    print(snake_case)

           



if __name__ == "__main__":
    main()
