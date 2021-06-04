"""tile
    
    Creates a Tile based that will be placed on the game surface.
    Tiles have rects that help at collision detection.
    
    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import pygame
from spritesheet import SpriteSheet
from constants import *

class Tile(pygame.sprite.Sprite):
    """Tiles object to determin collisions

    Args:
        pygame (Sprite): Inherits from pygame Sprite class
    """
    def __init__(self, image, spriteSheet, x, y):
        """creates a tile and creates a mask for collision detection

        Args:
            image (str): contains the name of the image to search for in the spriteSheet
            spriteSheet (Spritesheet): object of class to use all function regarding the work with spritesheets
            x (int): x position of the tile
            y (int): y position of the tile
            
        Test:
            * the creation of the goal tile must be recognized
            * the goal tile must be bigger than the other tiles
        """
        pygame.sprite.Sprite.__init__(self)
        
        self.image = spriteSheet.parseSprite(image)
        
        if image == GOAL:
            #TODO also needs to know what level it is (maybe the goal size changes)
            self.image = pygame.transform.scale(self.image, (BLOCK_SIZE*GOALL1_W, BLOCK_SIZE*GOALL1_H))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = pygame.mask.from_surface(self.image)
        
    def draw(self, surface):
        """draws the tiles on a given surface

        Args:
            surface (Surface): surface on which the tiles should be drawn on
            
        Test:
            * the tile must be drawn on the right place (rect)
            * the surface must containg the tile after blitting on it 
        """
        surface.blit(self.image, self.rect)