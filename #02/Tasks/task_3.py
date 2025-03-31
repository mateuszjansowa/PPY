from decimal import Decimal

def decimalSolution():
    sum = Decimal('0')
    for i in range (1_000_000):
        sum += Decimal('0.1')

    print(sum == Decimal('100_000.0'))

def main():
    sum = 0
    for i in range (1_000_000):
        sum += 0.1
    print(sum == 100_000.0)
    decimalSolution()

if __name__ == "__main__":
    main()