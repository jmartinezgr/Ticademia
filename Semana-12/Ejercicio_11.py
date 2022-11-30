mensajes = [
    "Hasta luego curso! Turing, puedes estar orgulloso de mi",
    "Goodbye course! Turing, you can be proud of me",
    "Au revoir cours! Turing, tu peux etre fier de moi",
    "Adeus, curso! Turing, pode se orgulhar de mim",
    "Auf Wiedersehen! Turing, du kannst stolz auf mich sein ",
    ]

n = int(input())
while n >= 5:
    print(mensajes[int(n%5)])
    n /= 5
