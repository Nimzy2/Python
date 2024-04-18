
from circum_functions import compute_area, compute_circumference

def main():
    radius = float(input("Enter the radius: "))
    circumference = compute_circumference(radius)
    area = compute_area(radius)
    print(f"The circumference of the circle is: {circumference:.3f} \nThe area of the circle is: {area:.3f}")


if __name__ == "__main__":
    main()