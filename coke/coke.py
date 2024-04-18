def main():
    print("Coke costs 50 cents")
    quantity = int(input("How many do you need? "))
    amount_due = 50 * quantity
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        amount_paid = int(input("insert a 25, 10, 5 cent coin: "))
        if amount_paid == 25 or amount_paid == 10 or amount_paid == 5:
            amount_due -= amount_paid
    print(f"change owed: {-1 * amount_due}")


if __name__ == "__main__":
    main()