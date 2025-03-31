def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            match number:
                case n if n > 0:
                    print("You entered a positive number.")
                case n if n < 0:
                    print("You entered a negative number.")
                case _ if n == 0:
                    print("You entered zero.")        
        except ValueError as e:
            print("Invalid input, please enter a number.")
            continue
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()