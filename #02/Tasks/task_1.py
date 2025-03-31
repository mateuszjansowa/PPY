def floatToOtherTypes(floatNumber):
    try:
        print("Float number: ", floatNumber, type(floatNumber))
        print("Int number: ", int(floatNumber), type(int(floatNumber)))
        print("String number: ", str(floatNumber), type(str(floatNumber)))
        print("Complex number: ", complex(floatNumber), type(complex(floatNumber)))    
    except ValueError as e:
        print(f"Blad konwersji: {e}")
    except TypeError as e:
        print(f"Niepoprawny typ danych: {e}")


def main():
    floatNumber = 3.1415
    floatToOtherTypes(floatNumber)

if __name__ == "__main__":
    main()