import pygame

class ShipBullet:

    def __init__(self, screen, x, y, direction):

        self.screen = screen

        self.speed = 8

        self.rect = pygame.Surface((5, 20)).get_rect()

        self.rect.x = x + 30
        self.rect.y = y - 20

        if direction == 1:
            self.down = True
        else:
            self.up = True

    def move(self):

        if self.up:
            self.rect.y -= self.speed
        elif self.down:
            self.rect.y += self.speed

    def refresh(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 0)