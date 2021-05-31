import os, sys
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from loguru import logger
import pickle

from menu import Menu


def main(test = False):
    pygame.init()
    
    savedValues = {"Cars":{"BasicCar":True, "CopCar":False, "F1Car":False, "SportsCar":False}, "Score":1000}
    #TODO Diese FileConst raus machen
    #TODO Try Catch drum, Wenn nicht gefunden wird muss default genommen werden
    with open(".\\score\\savedScore", "rb") as f:
        savedScore = pickle.load(f)

    # To remove the default stderr output
    logger.remove()
    logger.add(".\\logging\\loggingInfos.log" , level="INFO", mode="w")

    menu = Menu(savedScore)
    #TODO Hier am besten return vlaue ist savedValues
    menu.mainMenu(test)
    
    #TODO never reaches here
    #TODO Save score and cars into pickle
    with open(".\\score\\savedScore", "wb") as f:
        pickle.dump(savedValues, f)

if __name__ == "__main__":
    main()    