import pygame
import sys


NERO = (0, 0, 0 )       #rgb (x, y, z) -> 0 <= x,y,z => 255 
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

pavimento = [[0, 0, 0, -1, -1, 0, -1], #0 libero -1 occupato
                [-1, 0, 0, 0, -1, -1, 0], 
                [0, 0, -1, -1, -1, 0, 0], 
                [-1, 0, 0, 0, -1, -1, 0], 
                [-1, 0, 0, 0, 0, -1, -1], 
                [-1, -1, -1, 0, 0, 0, -1]] 

dimensione = 100

ALTEZZA = len(pavimento) * dimensione
LARGHEZZA = len(pavimento[0]) * dimensione

def disegnaOstacoli():
    for contY in range(0, len(pavimento)):
            for contX in range(0, len(pavimento[contY])):
                

                if pavimento[contY][contX] == -1:
                    contX = contX * dimensione
                    contY = contY * dimensione 

                    ostacolo = pygame.Rect(contX, contY, dimensione, dimensione)
                    pygame.draw.rect(screen, ROSSO, ostacolo)

                    contX = int(contX / dimensione)
                    contY = int(contY / dimensione) 

def numeraPavimento():
    global pavimento
    contCelle = 0

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            if pavimento[contY][contX] == 0:             
                pavimento[contY][contX] = contCelle
                contCelle += 1
                
                fnt = pygame.font.SysFont("Comic Sans", 25, bold = True)
                txt = fnt.render(str(contCelle), True, (255, 255, 255))
                screen.blit(txt, (contX * dimensione + 10, contY * dimensione + 10))

def drawGrid():
    dimensione = 100
    for x in range(0, LARGHEZZA, dimensione):
        for y in range(0, ALTEZZA, dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione)  #vertice alto-sinsitra, max lato
            pygame.draw.rect(screen, BIANCO, piastrella, 1)  #dove disegnare, colore, cosa, bordo (se nn metto niente o 0 fa disegno pieno)


def creaDizionario():
        dizCoord = {}
        spazLiberi = []
        numeraPavimento()

        for y in range (0, len(pavimento)):
            for x in range (0, len(pavimento[y])):

                if pavimento[y][x] != -1:

                    if x != 0:
                        if pavimento[y][x - 1] != -1:
                            spazLiberi.append(pavimento[y][x - 1])
                    
                    if x != len(pavimento[y]) - 1:
                        if pavimento[y][x + 1] != -1:
                            spazLiberi.append(pavimento[y][x + 1])
                    
                    if y != 0:
                        if pavimento[y - 1][x] != -1:
                            spazLiberi.append(pavimento[y - 1][x])
                    
                    if y != len(pavimento) - 1:
                        if pavimento[y + 1][x] != -1:
                            spazLiberi.append(pavimento[y + 1][x])
        
                    dizCoord[pavimento[y][x]] = spazLiberi
                    spazLiberi = [] 
        
        print(dizCoord)

def main():
    global screen
    pygame.init()  #parte pygame
    screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))  #dimensioni schermo
    screen.fill(NERO)

    
    creaDizionario()

    while True:
        drawGrid()
        disegnaOstacoli()
        for event in pygame.event.get():        #ascolta eventi (mouse, tastiera ecc)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        pygame.display.update()


if __name__ == "__main__":
    main()
