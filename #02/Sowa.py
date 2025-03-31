def main():
    result_list = []

    while True:
        line = input("Enter sizes: ").strip()

        if line == "":
            break

        numbers = line.split()

        try:
            numbers = tuple(map(int, numbers))
        except ValueError:
            print("Błąd: Wprowadź tylko liczby!")
            continue

        if len(numbers) == 1:
            shape = "S"  # Square
            area = numbers[0] ** 2
        elif len(numbers) == 2:
            shape = "R"  # Rectangle
            area = numbers[0] * numbers[1]
        elif len(numbers) == 3:
            shape = "C"  # Cuboid
            area = numbers[0] * numbers[1] * numbers[2]
        else:
            print("Błąd: Wprowadź 1, 2 lub 3 liczby!")
            continue

        result_tuple = (shape, numbers, area)
        result_list.append(result_tuple)

    print(result_list)

if __name__ == "__main__":
    main()