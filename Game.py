import pygame
from SpaceShip import *
from Alien import *
import time
import schedule
import random
import os

class Game:

    text = "text"

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("SpaceInvaders")

        self.running = True

        self.screen = pygame.display.set_mode((500, 720))
        
        self.ship = SpaceShip(self.screen,self)

        self.aliens = []

        schedule.every(1).seconds.do(self.spawnAlien)

        self.gameLoop()

    
    def spawnAlien(self):
        alien = Alien(self.screen, self, random.randint(10, 480), 0)
        self.aliens.append(alien)
        print("Un alien spawned")
    

    def refreshAliens(self):

        for alien in self.aliens:
            if alien.rect.y < 720:
                alien.move()
                alien.refresh()
            else:
                self.aliens.remove(alien)
    
    def refreshHUD(self):
        font = pygame.font.SysFont("Arial", 25)
        healthInfo = font.render("Vie: " + str(self.ship.health), False, (255, 255, 255), (0, 0, 0))
        KillsInfo = font.render("Aliens: " + str(self.ship.kills), False, (255, 255, 255), (0, 0, 0))
        BulletInfo = font.render("Munitions: " + str(self.ship.ammo), False, (255, 255, 255), (0, 0, 0))

        self.screen.blit(healthInfo, [10, 10, 100, 40])
        self.screen.blit(KillsInfo, [10, 40, 100, 40])
        self.screen.blit(BulletInfo, [10, 70, 100, 40])
        


    def gameLoop(self):

        #boucle de jeu

        while self.running:

            self.screen.fill((0,0,0))
            self.refreshHUD()
            self.ship.refresh(self.screen)
            self.refreshAliens()

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("Fermeture de la fenêtre")
                
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        self.ship.left = False
                        self.ship.right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.right = False
                        self.ship.left = True
                    
                    if event.key == pygame.K_UP:
                        self.ship.down = False
                        self.ship.up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.up = False
                        self.ship.down = True
                
                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_RIGHT:
                        self.ship.right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.left = False
                    
                    if event.key == pygame.K_UP:
                        self.ship.up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.down = False
                    
                    if event.key == pygame.K_SPACE:
                        self.ship.shootBullet()
            
            schedule.run_pending()
            pygame.time.delay(15)
    
        #end - Game Over
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 40)
        gameOver = font.render("Game Over", False, (255, 255, 255), (0, 0, 0))
        self.screen.blit(gameOver, [180, 300, 100, 30])
        pygame.display.flip()
        os.system("PAUSE")

            

                