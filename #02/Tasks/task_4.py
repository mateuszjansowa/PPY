def complexFromString(s):
    try:
        return complex(s)
    except ValueError as e:
        print(f"Blad konwersji: {e}")
    except TypeError as e:
        print(f"Niepoprawny typ danych: {e}")
    return None
    

def main():
    print(complexFromString(3.14))

if __name__ == "__main__":
    main()
