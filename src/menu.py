import pygame 
import pygame_menu
import pickle
from loguru import logger
from pygame_menu.locals import ALIGN_LEFT
from pygame_menu.themes import Theme
from constants import *
from game import Game

class Menu():
    
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.score = self.loadScore()
        self.surface = pygame.display.get_surface()
        
        self.background = pygame_menu.BaseImage(image_path=BACKIMAGE)
        
        self.coin = pygame_menu.BaseImage(image_path=COINIMAGE).resize(width=COIN_SIZE, height=COIN_SIZE)
        
        self.wKey = pygame_menu.BaseImage(image_path=WKEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.sKey = pygame_menu.BaseImage(image_path=SKEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.dKey = pygame_menu.BaseImage(image_path=DKEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.aKey = pygame_menu.BaseImage(image_path=AKEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.hKey = pygame_menu.BaseImage(image_path=HKEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.spaceKey = pygame_menu.BaseImage(image_path=SPACEKEY).resize(width=3*KEY_SIZE, height=KEY_SIZE)
        
        self.price50 = pygame_menu.BaseImage(image_path=PRICE50).resize(width=PRICE_W, height=PRICE_H)
        self.price100 = pygame_menu.BaseImage(image_path=PRICE100).resize(width=PRICE_W, height=PRICE_H)
        self.price200 = pygame_menu.BaseImage(image_path=PRICE200).resize(width=PRICE_W, height=PRICE_H)

        self.basicCar = pygame_menu.BaseImage(image_path=BASICCARIMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.f1Car = pygame_menu.BaseImage(image_path=F1IMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.copCar = pygame_menu.BaseImage(image_path=COPCARIMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.sportsCar = pygame_menu.BaseImage(image_path=SPORTCARIMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)

        self.decorator = []
        # Creating own Theme
        self.myTheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.myTheme = Theme(
                                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                #Menu titel is not used | To get rid of warning that titel and background have same color
                                title_font_color = BLACK,
                                widget_font_size = WIDGET_SIZE,
                                widget_font = pygame_menu.font.FONT_8BIT,
                                widget_margin = WIDGET_MARGIN,
                            )
        self.myTheme.set_background_color_opacity(BACKGROUND_OPACITY) #CONST HERE TODO
        
        self.carMenu = self.createCarMenu()
        self.controlsMenu = self.createControlsMenu()
        self.playMenu = self.createPlayMenu()
        
        logger.info("Menus initialized")
        
    def mainMenu(self):
        
        mainMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", onclose=pygame_menu.events.EXIT)
        
        # Creating different buttons to press
        decorator = mainMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)

        mainMenu.add.button("Play",self.playMenu)
        mainMenu.add.button("Choose Car", self.carMenu)
        mainMenu.add.button("Controls", self.controlsMenu)
        mainMenu.add.button("Exit", pygame_menu.events.EXIT)
        logger.info("Main Menu Buttons created")
        
        mainMenu.mainloop(self.surface, self.drawBackground, fps_limit=FPS)

    def createPlayMenu(self):
        #TODO Make columns rows dynamic with value of Levels
        playMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", columns=2, rows=3)
        
        decorator = playMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        playMenu.add.label(f"Level One")
        playMenu.add.image(self.basicCar)
        playMenu.add.button(f"PLAY", self.game.gameLoop, self.player, self, 1)
        
        playMenu.add.label(f"Level Two")
        playMenu.add.image(self.sportsCar)
        playMenu.add.button(f"PLAY")
        
        return playMenu
    
    def createCarMenu(self):
        #TODO column number generic with skin values
        #
        myTheme = self.myTheme.copy()
        myTheme.widget_font_size = 22
        carMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=myTheme, title=" ", columns=4, rows=3)
        
        decorator = carMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        #TODO Padding ugly - think again. If there is no solution leave it
        carMenu.add.label(f"FREE").set_padding((20,0,15,0))
        carMenu.add.image(self.basicCar)
        if(self.score["Cars"]["BasicCar"] == True):
            carMenu.add.button("Select",self.player.setImage, BASICCARIMAGE)
        
        carMenu.add.image(self.price50)
        carMenu.add.image(self.copCar)
        # Hide "select" button to switch it easily with the buy button
        copSelectBut = carMenu.add.button("Select",self.player.setImage, COPCARIMAGE).hide()
        if(self.score["Cars"]["CopCar"] == True):
            copSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar,"CopCar", copSelectBut, COPCARIMAGE).add_self_to_kwargs(key="widget")
        
        carMenu.add.image(self.price100)
        carMenu.add.image(self.f1Car)
        f1SelectBut = carMenu.add.button("Select", self.player.setImage, F1IMAGE).hide()
        if(self.score["Cars"]["F1Car"] == True):
            f1SelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "F1Car",f1SelectBut, F1IMAGE).add_self_to_kwargs(key="widget")
        
        carMenu.add.image(self.price200)
        carMenu.add.image(self.sportsCar)
        sportsSelectBut = carMenu.add.button("Select",self.player.setImage, SPORTCARIMAGE).hide()
        if(self.score["Cars"]["SportsCar"] == True):
            sportsSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "SportsCar",sportsSelectBut, SPORTCARIMAGE).add_self_to_kwargs(key="widget")
        
        logger.info("Car Menu created")
        return carMenu
    
    def createControlsMenu(self):
        
        controlsMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", columns=2, rows=6)
        
        decorator = controlsMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        controlsMenu.add.label("Forward").set_alignment(ALIGN_LEFT)
        controlsMenu.add.label("Backward").set_alignment(ALIGN_LEFT)
        controlsMenu.add.label("Left").set_alignment(ALIGN_LEFT)
        controlsMenu.add.label("Right").set_alignment(ALIGN_LEFT)
        controlsMenu.add.label("Emergency brake").set_alignment(ALIGN_LEFT)
        controlsMenu.add.label("Honk").set_alignment(ALIGN_LEFT)
        
        controlsMenu.add.image(self.wKey, margin=(0,0))
        controlsMenu.add.image(self.sKey, margin=(0,0))
        controlsMenu.add.image(self.aKey, margin=(0,0))
        controlsMenu.add.image(self.dKey, margin=(0,0))
        controlsMenu.add.image(self.spaceKey, margin=(0,0))
        controlsMenu.add.image(self.hKey, margin=(0,0))
        
        logger.info("Controls menu created")
        return controlsMenu
    
    def drawBackground(self):
        self.background.draw(self.surface)
    
    def purchaseCar(self, car, purchBut, widget, imagePath):
        if(car == "CopCar" and PRICECOPCAR <= self.score["Score"]):
            self.score["Cars"]["CopCar"] = True
            self.score["Score"] -= PRICECOPCAR
            widget.hide()
            purchBut.show()
        elif(car == "F1Car" and PRICEF1CAR <= self.score["Score"]):
            self.score["Cars"]["F1Car"] = True
            self.score["Score"] -= PRICEF1CAR
            widget.hide()
            purchBut.show()
        elif(car == "SportsCar" and PRICESPORTSCAR <= self.score["Score"]):
            self.score["Cars"]["SportsCar"] = True
            self.score["Score"] -= PRICESPORTSCAR
            widget.hide()
            purchBut.show()
        else:
            if(car == "CopCar" or car == "F1Car" or car == "SportsCar"):
                logger.info("Something went wrong purchasing a car >> Price to high")
            else:
                logger.debug("Something went wrong purchasing a car >> car not found")
        
        self.player.setImage(imagePath)
        self.updateScore()
        self.saveScore()
    
    def updateScore(self):
        for dec in self.decorator:
            dec.remove_all()
            self.addScore(dec)
    
    def addScore(self, decorator):
        #POS of text and image in const files
        decorator.add_text(y=SCORE_X, x=SCORE_TEXT_Y, text=str(self.score["Score"]), font=pygame_menu.font.FONT_8BIT, size=WIDGET_SIZE, color=BLACK)
        decorator.add_baseimage(y=SCORE_X, x=SCORE_COIN_Y, image=self.coin)
        logger.info("Updated Score")
    # Where did i use this
    def setScore(self, value):
        self.score["Score"] += value 
        self.updateScore()
        self.saveScore()
    
    def loadScore(self):
        try:
            with open(SCOREFILE, "rb") as f:
                savedScore = pickle.load(f)
        except:
            savedScore = {"Cars":{"BasicCar":True, "CopCar":False, "F1Car":False, "SportsCar":False}, "Score":0}
            logger.info(f"Score File not found >> Default values used: {self.score['Score']} , {self.score['Cars']}")
        
        return savedScore    
    
    def saveScore(self):
        try:
            with open(SCOREFILE, "wb") as f:
                pickle.dump(self.score, f)
            logger.info(f"Saved Information : {self.score['Score']} , {self.score['Cars']}")
        except:
            logger.info(f"Savong new score failed >> Check Path {SCOREFILE}")