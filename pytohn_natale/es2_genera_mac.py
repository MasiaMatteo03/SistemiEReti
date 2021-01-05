import random

caratteri = {"1": [48, 57],
            "2": [65, 70]}

def main():
    capacityMac = 6
    cnt = 0
    cntCouple = 0
    couple = 2
    mac = ""

    while cnt != capacityMac:

        while cntCouple != couple:
            typeCar = random.randint(1, 2)

            if typeCar == 1:
                mac = mac + chr(random.randint(caratteri["1"][0], caratteri["1"][1]))
            elif typeCar == 2:
                mac = mac + chr(random.randint(caratteri["2"][0], caratteri["2"][1]))
            cntCouple = cntCouple + 1
        cnt = cnt + 1
        if cnt == capacityMac:
            mac = mac + " "
        else:
            mac = mac + ":"
        cntCouple = 0
        
    
    print(mac)

if __name__ == "__main__":
    main()