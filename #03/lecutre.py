def main():
    while True:
        try:
            data = input("Enter your name: ")
            if data == "":
                raise ValueError("Input cannot be empty")
            
            print(f"Hello, {data}!")

        except ValueError as e:
            print(e)
            continue
        break 

# This code will keep asking for input until a valid name is provided

if __name__ == "__main__":
    main()