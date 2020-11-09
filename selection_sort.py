vett = [1,2,8,4,5,10,7,3,9,6]
print("\nVettore iniziale")
print(vett)

#algoritmo selection sort ordinamento vettore vett
for cnt in range (len(vett)):
    cntMin = cnt
    for i in range(cnt + 1, len(vett)):
        if vett[cntMin] > vett[i]:
            cntMin = cnt
            vett[cntMin], vett[i] = vett[i], vett[cntMin]
print("\nVettore ordinato")
print(vett)
