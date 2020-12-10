file = open("canzoni.csv", "r")  #open the file
playlist = []  #empty list
autore = ""  #empty string
titolo = ""  #empty string


for riga in file:  #read file
    #print(riga[0:-1].split(","))  print a list with the elements are in the row (from 0 to the last componet excluded) divided by the split
    line = riga[0:-1].split(",")  #split each line of the file and save it in the "line" variable
    appoggioAutore = autore.join(line[2])  #join the string "autore" in "line[2]
    appoggioTitolo = titolo.join(line[1])
    
    canzone = {"Numero":line[0], "Titolo":appoggioTitolo, "Autore":appoggioAutore}  #dictionary creation
    playlist.append(canzone)  #append the song "canzone" in playlist

print(f"{playlist} \n\nPlaylist: \n")  #print all the playlist

for canzone in playlist:    #print the each components of the playlist in line
    print(canzone["Numero"], "-", canzone["Titolo"], "-", canzone["Autore"])
file.close()
