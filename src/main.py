import os, sys
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import pickle

from loguru import logger
from constants import *
from menu import Menu
from player import Player
from game import Game
from spritesheet import SpriteSheet
from map import Map


def main():
    pygame.init()
    pygame.display.set_mode(WINDOWSIZE)
    pygame.display.set_caption("Parking 2D")
    
    # To remove the default stderr output
    logger.remove()
    logger.add(LOG_FILE , level="INFO", mode="w")

    player = Player(BASICCAR_IMAGE, START_X, START_Y)
    
    game = Game()
    menu = Menu(game, player)

    menu.mainMenu()

if __name__ == "__main__":
    main()    