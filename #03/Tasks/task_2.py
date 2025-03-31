def main():
    sum = 0

    while True:
        try:
            number = int(input("Enter a number: "))
            if number > 0:
                sum+=number
            elif number == 0:
                continue
            else:
                raise Exception("Negative number entered.")
        except ValueError as e:
            print("Invalid input:", e)
            break
        except Exception as e:
            print("Error occurred:", e)
            break

    print(f"Sum of positive numbers: {sum}")

if __name__ == "__main__":
    main()