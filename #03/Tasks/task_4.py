def main():
    try:
        userInput = input("Enter some numbers: ")
        numbers = list(map(int, userInput.split())) # split the input string to a list of ints

        match len(numbers):
            case 0:
                raise ValueError("No numbers provided")
            case 1:
                area = int(numbers[0]) ** 2
                print(f"Area of square: {area}")
            case 2:
                area = int(numbers[0] * numbers[1])
                print(f"Area of rectangle: {area}")
            case 3:
                area = 2 * (int(numbers[0]) * int(numbers[1]) + int(numbers[1]) * int(numbers[2]) + int(numbers[0]) * int(numbers[2]))
                print(f"Area of cuboid: {area}")
            case _:
                print("Unknown shape")

    except Exception as e:
        print(f"Threw error: {e}")

if __name__ == "__main__":
    main()