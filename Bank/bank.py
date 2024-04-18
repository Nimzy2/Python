def main():
    greeting = input("Enter greeting: ").strip() .lower()
    reward = compute_reward(greeting)
    print(reward)

    

def compute_reward(greeting):
    if greeting.startswith("hello"):
        return("$0")
    elif greeting.startswith("h"):
        return("$20")
    else:
        return("$100")


if __name__ == "__main__":
    main()
