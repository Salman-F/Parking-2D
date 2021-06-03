import pygame
from spritesheet import SpriteSheet
from constants import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, spriteSheet, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = spriteSheet.parseSprite(image)
        
        if image == GOAL:
            #TODO also needs to know what level it is
            self.image = pygame.transform.scale(self.image, (BLOCK_SIZE*GOALL1_W, BLOCK_SIZE*GOALL1_H))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = pygame.mask.from_surface(self.image)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)