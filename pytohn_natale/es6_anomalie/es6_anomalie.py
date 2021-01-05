def maxMinAnomalia(anomalieAnnuali):
    anno1 = int(input("Inserisci il primo anno\n"))
    anno2 = int(input("Inserisci il secondo anno\n"))


    maxMin = []
    for cnt in range(anno1, anno2 + 1):
        maxMin.append(float(anomalieAnnuali[str(cnt)]))
    
    print(f"MAX anomalia: {max(maxMin)}, MIN anomalia {min(maxMin)}")

def main():
    anomalieAnnuali = {}
    lineaSucc = 2
    counter = 1
    somma = 0
    media = 0
    data = open("annual.csv", "r").readlines()
    
    for line in data[1:]:
        if lineaSucc >= len(data):
            lineaSucc = 0
        line = line[:-1].split(",")
        line2 = data[lineaSucc].split(",")

        if line[1] == line2[1]:
            somma = somma + float(line[2])
            counter = counter + 1
        else:
            somma = somma + float(line[2])
            media = somma / counter
            anomalieAnnuali[line[1]] = media
            counter = 1
            somma = 0
        
        lineaSucc = lineaSucc + 1
    
    maxMinAnomalia(anomalieAnnuali)




if __name__ == "__main__":
    main()