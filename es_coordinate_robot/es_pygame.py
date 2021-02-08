import pygame
import sys
ALTEZZA = 600
LARGHEZZA = 600
NERO = (0, 0, 0 )       #rgb (x, y, z) -> 0 <= x,y,z => 255 
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

def drawGrid():
    dimensione = 50
    for x in range(0, LARGHEZZA, dimensione):
        for y in range(0, ALTEZZA, dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione)  #vertice alto-sinsitra, max lato
            pygame.draw.rect(screen, BIANCO, piastrella, 1)  #dove disegnare, colore, cosa, bordo (se nn metto niente o 0 fa disegno pieno)
    
    ostacolo = pygame.Rect(50, 100, dimensione, dimensione)
    pygame.draw.rect(screen, ROSSO, ostacolo)

def main():
    global screen
    pygame.init()  #parte pygame
    screen = pygame.display.set_mode((ALTEZZA, LARGHEZZA))  #dimensioni schermo
    screen.fill(NERO)

    while True:
        drawGrid()
        for event in pygame.event.get():        #ascolta eventi (mouse, tastiera ecc)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()