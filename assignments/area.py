def circle(r):
    area = 22/7 * r**2
    circum = 22/7 * 2 * r
    # result = (area, circum)
    result_1 = {"area":area, "circum":circum}
    return result_1


def main():
    radius = float(input("Radius: "))
    result = circle(radius)
    result["area"] = 500

    print(f'A circle of {radius} has an area of {result["area"]:.2f} and circumference of {result["circum"]:.2f}')



if __name__ == "__main__":
    main()