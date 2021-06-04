"""spritesheet
    
    Helps parsing sprites and returning the image of a Tile.
    
    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import pygame
import json

from loguru import logger

class SpriteSheet():
    """Manages the work with the given spritesheet
    """
    def __init__(self, file):
        """loads the spritesheet

        Note:
            Inspired by: https://www.youtube.com/watch?v=ePiMYe7JpJo
        
        Args:
            file (str): path to the given file
        
        Test:
            * the file ending must be changed to json
            * the json must be readabel 
        """
        self.file = file
        self.spriteSheet = pygame.image.load(file).convert()
        self.metaData = self.file.replace('png', 'json')
        
        logger.info(f"Json for spritesheet: {self.metaData}")

        with open(self.metaData) as f:
            self.data = json.load(f)
        
    def getSpriteImage(self, x, y, w, h):
        """gets the sprite image out of the spritesheet

        With the help of the image we can create a rect and a mask for the collision detection
        
        Args:
            x (int): x position of the image
            y (int): y position of the image
            w (int): width of the image
            h (int): height of the image

        Returns:
            Surface: surface containing the tile image
        
        Test:
            * the image must not be croped (the whole image must be drawn on the sprite surface)
            * the sprites surface should not be greater or less then the given width and height
        """
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((1,1,1))
        sprite.blit(self.spriteSheet,(0, 0),(x, y, w, h))
        return sprite
    
    def parseSprite(self,name):
        """parses the data from the json to get needed values

        Args:
            name (str): contains the name of the tile image

        Returns:
            Surface: surface containing the tile image
        
        Test:
            * a valid name must be found in the json
            * x, y, w, h must be correctly assigned
        """
        sprite = self.data["frames"][0][name]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSpriteImage(x, y, w, h)
        return image