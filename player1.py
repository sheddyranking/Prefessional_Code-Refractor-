import pygame


class Player:
    def __init__(self, x, y, size, color="red"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

        