def run():
    palabra = input("Introduce una palabra: \n")
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")


if __name__ == "__main__":
    print("I D E N T I F I C A R  P A L I N D R O M O S")
    run()
