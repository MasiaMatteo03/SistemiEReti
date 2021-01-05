import random

caratteri = {"1":[48, 57],
            "2":[65, 90], 
            "3":[97, 122]}

def main():
    capacityPassword = int(input("Digita 1 se vuoi una password semplice, 2 se la vuoi più complicata:\n"))
   
    if capacityPassword == 1:
        password = ""
        maxCar = 8
        cnt = 0

        while cnt != maxCar:
            car = random.randint(1, 3)
            if car == 1:
                password = password + chr(random.randint(caratteri["1"][0], caratteri["1"][1]))
            elif car == 2:
                password = password + chr(random.randint(caratteri["2"][0], caratteri["2"][1]))
            elif car == 3:
                password = password + chr(random.randint(caratteri["3"][0], caratteri["3"][1]))
            cnt = cnt + 1

        print(f"La tua password è:\n {password}")

    elif capacityPassword == 2:
        password = ""
        maxCar = 20
        cnt = 0

        while cnt != maxCar:
            car = random.randint(1, 3)
            if car == 1:
                password = password + chr(random.randint(caratteri["1"][0], caratteri["1"][1]))
            elif car == 2:
                password = password + chr(random.randint(caratteri["2"][0], caratteri["2"][1]))
            elif car == 3:
                password = password + chr(random.randint(caratteri["3"][0], caratteri["3"][1]))
            cnt = cnt + 1

        print(f"La tua password è:\n {password}")

if __name__ == "__main__":
    main()