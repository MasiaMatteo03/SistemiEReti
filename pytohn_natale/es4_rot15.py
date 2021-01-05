def encode(string):
    strEnc = ""
    for elemento in string:
        elemento = ord(elemento) + 15
        elemento = chr(elemento)
        strEnc = strEnc + elemento
    print(strEnc)

def decode(string):
    strDec = ""
    for elemento in string:
        elemento = ord(elemento) - 15
        elemento = chr(elemento)
        strDec = strDec + elemento
    print(strDec)

def main():
    choice = int(input("Inserisci 1 se devi decriptare la stringa o 2 per criptarla: "))

    if choice == 1:
        string = str(input("inserisci la stringa da decriptare: "))
        decode(string)
    elif choice == 2:
        string = str(input("inserisci la stringa da criptare: "))
        encode(string)

if __name__ == "__main__":
    main()