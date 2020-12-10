file = open("canzoni.csv", "r")  #open the file
playlist = []  #empty list
autore = ""  #empty string
titolo = ""  #empty string


for riga in file:  #read file
    #print(riga[0:-1].split(","))  printa una lista con gli elementi presenti nella riga divisi dalla split
    line = riga[0:-1].split(",")  
    appoggioAutore = autore.join(line[2])  #split each line of the file and save it in the "line" variable
    appoggioTitolo = titolo.join(line[1])
    
    canzone = {"Numero":line[0], "Titolo":appoggioTitolo, "Autore":appoggioAutore}  #dictionary creation
    playlist.append(canzone)  #append the song "canzone" in playlist

print(f"{playlist} \n\nPlaylist: \n")  #print all the playlist

for canzone in playlist:    #print the each components of the playlist to head
    print(canzone["Numero"], "-", canzone["Titolo"], "-", canzone["Autore"])
file.close()