from deep_functions import check_answer


def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    result = check_answer(ans)
    print(result)


if __name__ == "__main__":
    main()