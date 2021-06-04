"""map
    
    Creates the map based on the given layout.
    Analyzes layout and creates Tile objects that will be placed on the map surface.
    This map surface will then be placed on the game surface.
    
    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import pygame 
import csv
from loguru import logger
from tile import Tile
from constants import *
from spritesheet import SpriteSheet

class Map():
    """Analyzes the maplayout and creates tiles accordingly
    Creates a surface with just black, green, brown and grey tiles that are needed for the collision detection.
    On top of this surface a image will be placed that is shaped like the tiles.
    """
    def __init__(self, mapLayout):
        """calls all requierd functions to create the map

        Args:
            mapLayout (str): contains path to the csv that includes the mapLayout
        
        Test:
            * self.tiles must be not empty at the end
            * the created surface must have the same size as in WINDOWSIZE
        """
        self.blockSize = BLOCK_SIZE
        self.tiles = []
        self.spriteSheet = SpriteSheet(SPRITE_FILE)
        self.tilesLayout = self.loadLayout(mapLayout)
        self.mapSurface = pygame.Surface(WINDOWSIZE)
        self.mapSurface.set_colorkey((0,0,0))
        self.loadTiles()
        logger.info(f"Map created")
        
    def loadLayout(self, mapLayout):
        """loads the csv and creates a list with all the data

        Args:
            mapLayout (str): contains path to the csv that includes the mapLayout

        Returns:
            list: includes the contant of the csv file
        
        Test:
            * the given file must be a csv
            * the returned list can not be empty
        """
        layout = []
        
        with open(mapLayout, newline="") as csvfile:
            seperatedCSV = csv.reader(csvfile, delimiter=",")
            
            for row in seperatedCSV:
                layout.append(list(row))
                logger.info(f"{row}")
        
        return layout
    
    def drawMap(self, surface):
        """draws the map on the given surface

        Args:
            surface (Surface): surface on which the map will be drawen
        
        Test:
            * the topleft corner of the mapSurface must be placed at (0,0) on the given surface
        """
        surface.blit(self.mapSurface, (0,0))
    
    def loadTiles(self):
        """loads the tiles from the created layout and draws them on the map surface
        
        Test:
            * the tile must be placed in the map surface
            * every tile must be iterated through
            * just valid tiles should be iterated
        """
        self.tiles = self.createTiles()
        for tile in self.tiles:
            tile.draw(self.mapSurface)
    
    def createTiles(self):
        """iterates the mapLayout and creates Tiles at the right x and y position

        Returns:
            list: contains all of the created Tiles
        
        Test:
            * created tiles must be on the right position
            * the goal must be bigger than a ordinary tile
        """
        tiles = []
        # To calculate the exact position the tile must be in
        x = 0
        y = 0        
        for row in self.tilesLayout:
            x = 0
            for tile in row:
                if tile == str(1):
                    self.goal = Tile("brown.png",self.spriteSheet, x*self.blockSize, y*self.blockSize)
                    logger.info(f"Goal size is {self.goal.rect}")
                elif tile == str(0) or tile == str(2) or tile == str(3):
                    tiles.append(Tile("black.png", self.spriteSheet, x*self.blockSize, y*self.blockSize))
                else:
                    if tile != str(-1):
                        logger.debug(f"Tile number {tile} not found, cant create a tile!! >> most likely dirty tile")
                x += 1
            y += 1
        return tiles