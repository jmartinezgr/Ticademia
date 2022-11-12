def español_morse(frase):
    equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    ".": ".-.-.-",
    ",": "-.-.--"} 

    string = ''
    frase= frase.split()
    for i in range(len(frase)):
        palabra = frase[i].upper()
        for h in palabra:
            string+=f'{equivalencias[h]} '
        if i != len(frase)-1:
            string += '/ '

    string += '\n'

    return string

n = int(input())
string_final = ''
for i in range(n):
    string_final+= español_morse(input()) 
    string_final += '\n'

print(string_final)


