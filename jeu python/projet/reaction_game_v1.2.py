import pygame
import random
import time
import sys
import requests
import RPi.GPIO as GPIO
pins = {
    2: 22,  #numéro du pin de la led en fonction de la case d jeu qui correspond
    3: 5,
    4: 16,
    5: 18  
}
touch = {
    24: pygame.K_f, #associe aux touches du clavier les touch sensor correspondants.
    26: pygame.K_g
    }

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p=GPIO.PWM(12,100)
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
for pin in touch:
    GPIO.setup(pin,GPIO.IN)
    
touch_state={
    24: 0, # permet de faire en sorte qu'un appui sur un touch compte pour une seule itération.
    26: 0
    }


def led_on(col):
    GPIO.output(pins[col], 1)
def led_off(col):
    GPIO.output(pins[col], 0)

def leds_off_all():
    for pin in pins.values():
        GPIO.output(pin, 0)


pygame.init()# initialise la fenêtre de jeu pygame
clock=pygame.time.Clock() #raccourci pour le module time qu'on utilise plus bas
font = pygame.font.SysFont('Copperplate', 36) #initialise une police d'écriture


class Grid:  # création de la grille de jeu et de ses méthodes

    def __init__(self, w=8, h=5, scale=60):
        self.columns = w  # nombre de colonnes
        self.lines = h  # nombre de lignes
        self.scale = scale  # longueur du carré de base
        self.width = self.columns * self.scale  # largeur de l'écran de jeu
        self.height = self.lines * self.scale  # hauteur de l'écran de jeu
        self.cells: list = [["null" for _ in range(self.lines)] for _ in range(self.columns)]  # liste comportant toutes les cellules ainsi que leur état


    def state(self, x: int, y: int, state):  # méthode pour changer l'état d'une case
        if state == "col1": #état éteint (rouge obscur)
            self.cells[x][y] = "col1"
        elif state == "col1ON":
            self.cells[x][y] = "col1ON" #état allumé (rouge vif)
        else:
            self.cells[x][y] = "null" #état rien (couleur noire)


    def draw(self):  # méthode d'affichage des cellules sur l'écran de jeu
        for x in range(self.columns):
            for y in range(self.lines):
                if self.cells[x][y] == "col1":
                    pygame.draw.rect(screen, (155, 0, 30), (x * self.scale, y * self.scale, self.scale, self.scale))
                elif self.cells[x][y] == "col1ON":
                    pygame.draw.rect(screen, (255,100,130), (x * self.scale, y * self.scale, self.scale, self.scale))

def controls(event,score): #verifie si on a touché une lumière allumée ou non, si oui elle augmente le score et en allume une autre, si non elle baisse le score
    if event == pygame.K_s and grid.cells[2][2]=="col1ON":
        grid.cells[2][2]="col1"
        led_off(2)
        nb = random.choice([3,4,5])
        grid.cells[nb][2] = "col1ON"
        led_on(nb)
        p.ChangeFrequency(440)
        p.start(5)
        return 1
    elif event == pygame.K_d and grid.cells[3][2]=="col1ON":
        grid.cells[3][2]="col1"
        led_off(3)
        nb = random.choice([2, 4, 5])
        grid.cells[nb][2] = "col1ON"
        led_on(nb)
        p.ChangeFrequency(440)
        p.start(5)
        return 1
    elif event == pygame.K_f and grid.cells[4][2]=="col1ON":
        grid.cells[4][2]="col1"
        led_off(4)
        nb = random.choice([2, 3, 5])
        grid.cells[nb][2] = "col1ON"
        led_on(nb)
        p.ChangeFrequency(440)
        p.start(5)
        return 1
    elif event == pygame.K_g and grid.cells[5][2]=="col1ON":
        grid.cells[5][2]="col1"
        led_off(5)
        nb = random.choice([2, 3, 4])
        grid.cells[nb][2] = "col1ON"
        led_on(nb)
        p.ChangeFrequency(440)
        p.start(5)
        return 1
    else:
        p.ChangeFrequency(200)
        p.start(5)
        return -1



grid = Grid() #création de la matrice de cellules

grid.state(5, 2, "col1")  #initialisation des cellules
grid.state(2, 2, "col1")
grid.state(3, 2, "col1")
grid.state(4, 2, "col1")

screen = pygame.display.set_mode((grid.width, grid.height))  # initialisation de la fenêtre de jeu
pygame.display.set_caption("THE REACTION GAME") #titre


def game():
    
    frames=0 #compteur de frames
    score = 0 #compteur de score
    start_time=time.time() 
    bip_frame=-5
    now_time=0
    
    while now_time<60:  # boucle faisant tourner le jeu

        now_time=time.time()-start_time # variable contenant le temps depuis le début du jeu

        frames += 1 #compteur de frames

        if frames==120: #le jeu débute au bout de 2 secondes
            nb=random.randint(2,5)
            grid.cells[nb][2]="col1ON"

        if frames-bip_frame==12:
            p.stop()
        
        screen.fill((0, 0, 0))  # rafraichissement de l'écran
        score_text = font.render(f"Score : {score}", True, (255, 255, 255))
        timer_text = font.render(f"Temps : {60-(frames//60)}s", True, (255, 255, 255))
        screen.blit(score_text, (2 * grid.scale, 1 * grid.scale))
        screen.blit(timer_text, (2 * grid.scale, 3 * grid.scale))

        grid.draw()

        for pin,key in touch.items(): 
            if GPIO.input(pin) == 1 and touch_state[pin]==0:
                bip_frame = frames
                score += controls(key, score)
            touch_state[pin] = GPIO.input(pin) #ca check si le touch été déja appuyé avant pour éviter de le recompter.
        
        
        for event in pygame.event.get(): #methode de vérification des inputs

            if event.type == pygame.QUIT:  # si on ferme la fenêtre de jeu
                now_time = 100  # alors on sort de la boucle while et on arrête ainsi le jeu

            if event.type == pygame.KEYDOWN: #si on clique sur une touche, on joue
                bip_frame = frames
                score+=controls(event.key,score)

        clock.tick(60)  # on rafraichit l'écran (on fait toutes les actions présentes dans la boucle while 60 fois par seconde)

        pygame.display.update()  # on actualise l'écran
    running=False
    p.stop()
    leds_off_all()
    return score  # on affiche alors le score

def send_score(score): #fonction pour envoyer le code au site
    try:
        requests.post(
            "http://127.0.0.1:5000/score",
            json={"score": score}
        )
    except:
        pass


final_score = game() # lance le jeu et lance le score 
send_score(final_score) # envoie le score final
try:
    import webbrowser
    webbrowser.open(f"http://localhost/leaderboard?score={final_score}") #ouvre la page du leaderboard
except:
    pass

pygame.quit()  # si on sort de la boucle while alors le programme s'arrête
sys.exit() #le script python s'arrête
