import pygame 
import csv
from loguru import logger
from tile import Tile
from constants import *
from spritesheet import SpriteSheet

#TODO Konstanten alle noch raus schreiben
class Map():
    def __init__(self, mapLayout):
        self.blockSize = BLOCK_SIZE
        self.tiles = []
        self.spriteSheet = SpriteSheet(SPRITEFILE)
        self.tilesLayout = self.loadLayout(mapLayout)
        # TODO Hier nochmal nach den maßen gucken
        self.mapSurface = pygame.Surface(WINDOWSIZE)
        self.mapSurface.set_colorkey((0,0,0))
        self.loadTiles()
        logger.info(f"Map created")
        
    def loadLayout(self, mapLayout):
        layout = []
        
        with open(mapLayout, newline="") as csvfile:
            seperatedCSV = csv.reader(csvfile, delimiter=",")
            
            for row in seperatedCSV:
                layout.append(list(row))
                logger.info(f"{row}")
        
        return layout
    
    def drawMap(self, surface):
        surface.blit(self.mapSurface, (0,0))
    
    def loadTiles(self):
        self.tiles = self.createTiles()
        for tile in self.tiles:
            tile.draw(self.mapSurface)
    
    def createTiles(self):
        tiles = []
        x = 0
        y = 0        
        for row in self.tilesLayout:
            x = 0
            for tile in row:
                logger.info(tile)
                if tile == str(1):
                    self.goal = Tile("brown.png",self.spriteSheet, x*self.blockSize, y*self.blockSize)
                    logger.info(f"Goal size is {self.goal.rect}")
                elif tile == str(0) or tile == str(2) or tile == str(3):
                    tiles.append(Tile("black.png", self.spriteSheet, x*self.blockSize, y*self.blockSize))
                else:
                    logger.info(f"Tile number not found, cant create a tile!!")
                x += 1
            y += 1
        return tiles