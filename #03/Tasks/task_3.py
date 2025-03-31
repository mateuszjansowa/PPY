from math import isqrt

def isPrime(n):
    if (n < 2):
        return False
    
    for i in range(2, isqrt(n) + 1):
        if (n % i == 0):
            return i
        
    return True


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                raise ValueError("Negative number entered.")
            elif number == 0:
                print("You entered zero.")
                continue

            result = isPrime(number)
            if result is True:
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number. First divisor: {result}")
        except ValueError as e:
            print("Invalid input:", e)
            break
        except Exception as e:
            print("Error occurred:", e)
            break

if __name__ == "__main__":
    main()
