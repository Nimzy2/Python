def main():
    num = int(input("Enter number: "))
    prime_factors = find_prime_factors(num) 
    print(prime_factors)


def find_prime_factors(num):
    prime_factors = []
    if num < 2:
        return prime_factors
    if  num >= 2:
        prime_factors.append(num)
    return prime_factors
    


if __name__ == "__main__":
    main()