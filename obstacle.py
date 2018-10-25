import pygame
import random

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface((width,height))
        #self.image.fill(color)
        taxiList = ['taxi1.png', 'taxi2.png', 'taxi3.png']
        taxiIndex = random.randrange(0,3)
        self.image = pygame.image.load(taxiList[taxiIndex])
        self.rect = self.image.get_rect()

    def update(self,backgroundRollChange):
        self.rect.y += backgroundRollChange
