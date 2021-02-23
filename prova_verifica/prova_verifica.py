import pygame
import sys
import random

NERO = (0, 0, 0 )       #rgb (x, y, z) -> 0 <= x,y,z => 255 
BIANCO = (92, 77, 102)
POS_INIZIALE = (0, 0, 255)
VIOLA = (198, 112, 255)
POS_FINALE = (199, 179, 0)

dimensione = 10
ALTEZZA = 410
LARGHEZZA = 410

def drawGrid():
    for x in range(0, LARGHEZZA, dimensione):
        for y in range(0, ALTEZZA, dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione)  #vertice alto-sinsitra, max lato
            pygame.draw.rect(screen, BIANCO, piastrella, 1)  #dove disegnare, colore, cosa, bordo (se nn metto niente o 0 fa disegno pieno)

def main():
    global screen

    spost = {0:[0,0]}
    coord = ()

    maxPerditaMin = 60
    cont = 0
    offset = 200
    x = 0
    y = 0

    pygame.init()  #parte pygame
    screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))  #dimensioni schermo
    screen.fill(NERO)

    file = open("percorso.csv", "w")
    file.write(f"{cont}: {x,y}\n")

    while True:    
        bob = pygame.Rect(offset, offset, dimensione, dimensione)
        pygame.draw.rect(screen, POS_INIZIALE, bob)
        drawGrid()
        
        
        for event in pygame.event.get():        #ascolta eventi (mouse, tastiera ecc)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        while cont != maxPerditaMin:
            choice = 0
            choice = random.randint(0, 3)

            if choice == 0:     #nord 
                y = y - dimensione
                bob = pygame.Rect(x + offset, y + offset, dimensione, dimensione)
                pygame.draw.rect(screen, VIOLA, bob)
                print("nord")
            
                cont = cont + 1
            elif choice == 1:       #sud
                y = y + dimensione
                bob = pygame.Rect(x + offset, y + offset, dimensione, dimensione)
                pygame.draw.rect(screen, VIOLA, bob)
            
                cont = cont + 1
                print("sud")
            elif choice == 2:       #est
                x = x + dimensione 
                bob = pygame.Rect(x + offset, y + offset, dimensione, dimensione)
                pygame.draw.rect(screen, VIOLA, bob)
                print("est")
            
                cont = cont + 1
            elif choice == 3:       #ovest
                x = x - dimensione
                bob = pygame.Rect(x + offset, y + offset, dimensione, dimensione)
                pygame.draw.rect(screen, VIOLA, bob)
                print("ovest")
            
                cont = cont + 1
            spost[cont] = [x,y]
            file.write(f"{cont}: {x,y}\n")
        file.close()
        bob = pygame.Rect(x + offset, y + offset, dimensione, dimensione)
        pygame.draw.rect(screen, POS_FINALE, bob)
        drawGrid()
        
        pygame.display.update()


if __name__ == "__main__":
    main()