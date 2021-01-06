def serieFib(num, max):
    if num != int(max):
        if num == 0 or num == 1:
            print(num)
            serieFib(num + 1, max)
        else:
            print((num - 1) + (num - 2))
            serieFib(num + 1, max)
        
def main():
    valMax = input("Inserisci il valore massimo per la serie:")
    cnt = 0
    serieFib(cnt, valMax)

if __name__ == "__main__":
    main()