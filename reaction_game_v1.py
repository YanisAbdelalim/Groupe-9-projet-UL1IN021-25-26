import pygame
import random
import time
pygame.init()
clock=pygame.time.Clock() #raccourci pour le module time qu'on utilise plus bas

frames = 0 #compteur de frames
score = 0
class Grid:  # création de la grille de jeu et de ses méthodes

    def __init__(self, w=8, h=5, scale=60):
        self.columns = w  # nombre de colonnes
        self.lines = h  # nombre de lignes
        self.scale = scale  # longueur du carré de base
        self.width = self.columns * self.scale  # largeur de l'écran de jeu
        self.height = self.lines * self.scale  # hauteur de l'écran de jeu
        self.cells: list = [["null" for _ in range(self.lines)] for _ in range(self.columns)]  # liste comportant toutes les cellules ainsi que leur état
        for x in range(self.lines):  # mise en place des bordures
            self.cells[0][x] = "border"
            self.cells[-1][x] = "border"
        for y in range(self.columns):
            self.cells[y][0] = "border"
            self.cells[y][-1] = "border"


    def state(self, x: int, y: int, state):  # méthode pour changer l'état d'une case
        if state == "col1":
            self.cells[x][y] = "col1"
        elif state == "col1ON":
            self.cells[x][y] = "col1ON"
        else:
            self.cells[x][y] = "null"


    def draw(self):  # méthode d'affichage des cellules sur l'écran de jeu
        for x in range(self.columns):
            for y in range(self.lines):
                if self.cells[x][y] == "col1":
                    pygame.draw.rect(screen, (155, 0, 30), (x * self.scale, y * self.scale, self.scale, self.scale))
                elif self.cells[x][y] == "col1ON":
                    pygame.draw.rect(screen, (255,100,130), (x * self.scale, y * self.scale, self.scale, self.scale))
                elif self.cells[x][y] == "border":
                    pygame.draw.rect(screen, (237, 34, 89), (x * self.scale, y * self.scale, self.scale, self.scale))

def controls(event):
    global score,nscore
    if event == pygame.K_s and grid.cells[2][2]=="col1ON":
        grid.cells[2][2]="col1"
        nb = random.choice([3,4,5])
        grid.cells[nb][2] = "col1ON"
        score+=1
    elif event == pygame.K_d and grid.cells[3][2]=="col1ON":
        grid.cells[3][2]="col1"
        nb = random.choice([2, 4, 5])
        grid.cells[nb][2] = "col1ON"
        score += 1
    elif event == pygame.K_f and grid.cells[4][2]=="col1ON":
        grid.cells[4][2]="col1"
        nb = random.choice([2, 3, 5])
        grid.cells[nb][2] = "col1ON"
        score += 1
    elif event == pygame.K_g and grid.cells[5][2]=="col1ON":
        nb = random.choice([2, 3, 4])
        grid.cells[nb][2] = "col1ON"
        grid.cells[5][2]="col1"
        score += 1
    else:
        score-=1



grid = Grid()

grid.state(5, 2, "col1")
grid.state(2, 2, "col1")
grid.state(3, 2, "col1")
grid.state(4, 2, "col1")

screen = pygame.display.set_mode((grid.width, grid.height))  # initialisation de la fenêtre de jeu
pygame.display.set_caption("THE REACTION GAME")

start_time=time.time()
now_time=0
while now_time<32:  # boucle faisant tourner le jeu
    now_time=time.time()-start_time

    frames += 1

    if frames==120:
        nb=random.randint(2,5)
        grid.cells[nb][2]="col1ON"

    screen.fill((0, 0, 0))  # rafraichissement de l'écran

    grid.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # si on ferme la fenêtre de jeu
            now_time = 100  # alors on sort de la boucle while et on arrête ainsi le jeu

        if event.type == pygame.KEYDOWN:
            controls(event.key)

    clock.tick(60)  # on rafraichi l'écran (on fait toutes les actions présentes dans la boucle while 60 fois par seconde)

    pygame.display.update()  # on actualise l'écran

print("Score: " + str(score))  # on affiche alors le score

pygame.quit()  # si on sort de la boucle while alors le programme s'arrête

