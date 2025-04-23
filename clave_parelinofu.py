

text_to_encode = input("Ingrese el texto que desea encriptar: ").lower()
codified = ""


for word in text_to_encode:
    for char in word:
        if char == "p":
                    char = "a"
                    codified+=char
        elif char == "a":
                char = "p"
                codified+=char
        elif char == "r":
                char = "e"
                codified+=char
        elif char == "e":
                    char = "r"
                    codified+=char
        elif char == "l":
                    char = "i"
                    codified+=char
        elif char == "i":
                    char = "l"
                    codified+=char
        elif char == "n":
                    char = "o"
                    codified+=char
        elif char == "o":
                    char = "n"
                    codified+=char
        elif char == "f":
                    char = "u"
                    codified+=char
        elif char == "u":
                    char = "f"
                    codified+=char
        else:
                codified+=char

print(codified)
