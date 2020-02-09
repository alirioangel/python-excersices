KEYS = {

    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',
    'A': '01000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'O': '01001111',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',
    '0': '00000000',
    '1': '00000001',
    '2': '00000010',
    '3': '00000011',
    '4': '00000100',
    '5': '00000101',
    '6': '00000110',
    '7': '00000111',
    '8': '00001000',
    '9': '00001001',
    '.': '00001010',
    ',': '00001011',
    '?': '00001100',
    '!': '00001101',
}


def cypher(message):
    words = message.split(" ")
    cypher_message = []

    for word in words:
        cypher_word = ""
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return " ".join(cypher_message)


def decipher(message):
    words = message.split(" ")
    decipher_message = []

    for word in words:
        decipher_word = ""

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return " ".join(decipher_message)


def run():

    while True:

        command = input(
            """--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografia a binarios. ¿Que deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        """
        )

        if command == "c":
            message = input("Escribe tu mensaje: ")
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == "d":
            message = input("Escribe tu mensaje tu cifrado: ")
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == "s":
            print("salir")
            break
        else:
            print("¡Comando no encontrado!")


if __name__ == "__main__":
    print("M E N S A J E S  C I F R A D O S")
    run()
