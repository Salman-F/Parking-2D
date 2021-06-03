import pygame
import json

from loguru import logger

class SpriteSheet():
    def __init__(self, file):
        self.file = file
        self.spriteSheet = pygame.image.load(file).convert()
        self.metaData = self.file.replace('png', 'json')
        
        logger.info(f"Json for spritesheet: {self.metaData}")

        with open(self.metaData) as f:
            self.data = json.load(f)
        
    def getSpriteImage(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((1,1,1))
        sprite.blit(self.spriteSheet,(0, 0),(x, y, w, h))
        return sprite
    
    def parseSprite(self,name):
        sprite = self.data["frames"][0][name]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSpriteImage(x, y, w, h)
        return image
