import pygame
from ShipBullet import *

class SpaceShip:


    def __init__(self, screen, game):
        
        self.health = 3
        self.kills = 0
        self.ammo = 30

        self.bullets = []

        self.screen = screen
        self.game = game

        self.speed = 7

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.sprite = pygame.transform.scale(pygame.image.load("assets/spaceShip.png"), (50, 20))

        self.rect = self.sprite.get_rect()

        self.rect.x = 240
        self.rect.y = 400

    def move(self):
        #Move spaceShip
        if self.right:
            self.rect.x += self.speed
        elif self.left:
            self.rect.x -= self.speed
        
        if self.up:
            self.rect.y -= self.speed
        elif self.down:
            self.rect.y += self.speed

        #move all bullets
        for bullet in self.bullets:
            bullet.move()

    def shootBullet(self):
        if self.ammo > 0:
            bullet = ShipBullet(self.screen, self.rect.x, self.rect.y, 0)
            self.bullets.append(bullet)
            self.ammo -= 1

    def refresh(self, screen):
        #Refresh spaceShip
        self.move()
        screen.blit(self.sprite, self.rect)
        #Refresh all bullets
        for bullet in self.bullets:
            bullet.move()
            bullet.refresh()
        
        for alien in self.game.aliens:
            if self.rect.colliderect(alien.rect):
                #Remove the collided alien
                self.game.aliens.remove(alien)
                #Damage the ship
                self.health -= 1
                #Check if ship is alive
                if self.health <= 0:
                    #stop the game
                    self.game.running = False