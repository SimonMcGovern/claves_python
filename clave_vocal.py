exchange = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}

text_to_encode = input("Inserte el texto que desea encriptar: ").lower()

for char in exchange.keys():
    text_to_encode = text_to_encode.replace(char, exchange[char])


print(text_to_encode)