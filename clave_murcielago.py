exchange = {"m": "0", "u": "1", "r": "2", "c": "3", "i" : "4", "e": "5", "l":"6", "a": "7",
            "g": "8", "o":"9", "ó":"9", "á": "7", "ú": "1", "í": "4", "é": "5"}

text_to_encode = input("Ingrese el texto que desea encriptar: ").lower()

for char in exchange.keys():
    text_to_encode = text_to_encode.replace(char, exchange[char])

print(text_to_encode)