import pygame
import main

class Alien:


    def __init__(self, screen, game, x, y):

        self.screen = screen

        self.game = game

        self.speed = 1

        self.sprite = pygame.transform.scale(pygame.image.load("assets/alien.png"), (30, 30))

        self.rect = self.sprite.get_rect()

        self.rect.x = x
        self.rect.y = y
    
    def move(self):
        self.rect.y += self.speed

    def refresh(self):
        self.move()
        self.screen.blit(self.sprite, self.rect)
        for bullet in self.game.ship.bullets:
            if self.rect.colliderect(bullet.rect):
                self.onCollide()
                self.game.ship.bullets.remove(bullet)
                self.game.ship.kills += 1



    def onCollide(self):
        #onCollide
        self.remove()
    

    def remove(self):
        self.game.aliens.remove(self)