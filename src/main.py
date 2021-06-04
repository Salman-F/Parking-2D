"""main

    Main function that creates the main Objects and starts the main loop.  

    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import os, sys
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from loguru import logger
from constants import *
from menu import Menu
from player import Player
from game import Game
from spritesheet import SpriteSheet
from map import Map


def main():
    """main function that initializes objects and starts mainloop
    
    Test:
        * display caption must be "Parking 2D"
        * display size must match WINDOWSIZE (declared in constants.py)
        * logging should not print anything in to the console
    """
    pygame.init()
    pygame.display.set_mode(WINDOWSIZE)
    pygame.display.set_caption("Parking 2D")
    pygame.mixer.music.load(MUSIC)
    pygame.mixer.music.play(-1)
    
    # To remove the default stderr output
    logger.remove()
    # Overwrite the last log file (because if you didnt immediately look at it the information is not important)
    logger.add(LOG_FILE , level="DEBUG", mode="w")

    player = Player(BASICCAR_IMAGE, START_X, START_Y)
    
    game = Game()
    
    menu = Menu(game, player)

    menu.mainMenu()

if __name__ == "__main__":
    main()    