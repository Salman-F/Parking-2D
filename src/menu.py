"""menu

    Displays the menu and handels input from user.

    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""

import pygame 
import pygame_menu
import pickle
from loguru import logger
from pygame_menu.locals import ALIGN_LEFT
from pygame_menu.themes import Theme
from constants import *
from game import Game

class Menu():
    """Controls the flow of the program based on the user.
        Handels all menus and redirects to functions at userinput.
    """
    
    def __init__(self, game, player):
        """Loads images, creates theme and more for main and submenus

        Args:
            game (Game): game object to call main gameloop
            player (Player): player object to change images
            
        Test:
            * The submenus must be initialized at the end
            * the images must be resized as implemented
        """
        self.game = game
        self.player = player
        self.score = self.loadScore()
        self.surface = pygame.display.get_surface()
        
        self.background = pygame_menu.BaseImage(image_path=BACK_IMAGE)
        
        self.coin = pygame_menu.BaseImage(image_path=COIN_IMAGE).resize(width=COIN_SIZE, height=COIN_SIZE)
        # Loads keyboards images
        self.wKey = pygame_menu.BaseImage(image_path=W_KEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.sKey = pygame_menu.BaseImage(image_path=S_KEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.dKey = pygame_menu.BaseImage(image_path=D_KEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.aKey = pygame_menu.BaseImage(image_path=A_KEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.hKey = pygame_menu.BaseImage(image_path=H_KEY).resize(width=KEY_SIZE, height=KEY_SIZE)
        self.spaceKey = pygame_menu.BaseImage(image_path=SPACE_KEY).resize(width=3*KEY_SIZE, height=KEY_SIZE)
        # Loads price images to visualize above cars
        self.price50 = pygame_menu.BaseImage(image_path=PRICE_50).resize(width=PRICE_W, height=PRICE_H)
        self.price100 = pygame_menu.BaseImage(image_path=PRICE_100).resize(width=PRICE_W, height=PRICE_H)
        self.price200 = pygame_menu.BaseImage(image_path=PRICE_200).resize(width=PRICE_W, height=PRICE_H)
        # Loads car images
        self.basicCar = pygame_menu.BaseImage(image_path=BASICCAR_IMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.f1Car = pygame_menu.BaseImage(image_path=F1_IMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.copCar = pygame_menu.BaseImage(image_path=COPCAR_IMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        self.sportsCar = pygame_menu.BaseImage(image_path=SPORTCAR_IMAGE).resize(width=MENU_CAR_W, height=MENU_CAR_H).rotate(PLAYER_INIT_ROT)
        # Loads Level previews
        self.levelOnePreview = pygame_menu.BaseImage(image_path=LEVELONE_BACKIMAGE).resize(width=PREVIEW_W, height=PREVIEW_H)
        self.comingSoon = pygame_menu.BaseImage(image_path=COMING_SOON).resize(width=PREVIEW_W, height=PREVIEW_H)
        self.decorator = []
        # Creating own Theme
        self.myTheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.myTheme = Theme(
                                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                #Menu titel is not used | To get rid of warning that titel and background have same color
                                title_font_color = BLACK,
                                title_font_size = FONT_SIZE_GAME + 10,
                                widget_font_size = WIDGET_SIZE,
                                widget_font = pygame_menu.font.FONT_8BIT,
                                widget_margin = WIDGET_MARGIN
                            )
        self.myTheme.set_background_color_opacity(BACKGROUND_OPACITY) #CONST HERE TODO
        
        self.carMenu = self.createCarMenu()
        self.settingsMenu = self.createSettingsMenu()
        self.controlsMenu = self.createControlsMenu()
        self.playMenu = self.createPlayMenu()
        
        logger.info("Menus initialized")
    
    def mainMenu(self):
        """Controls the main menu and shows buttons that redirect to other submenus
        
        Test:
            * Menu must be the same size as WINDOWSIZE
            * buttons must be drawn on the main menu and must be clickable
        """
        
        mainMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", onclose=pygame_menu.events.EXIT)
        
        # Creating different buttons to press
        decorator = mainMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)

        mainMenu.add.button("Play",self.playMenu)
        mainMenu.add.button("Choose Car", self.carMenu)
        mainMenu.add.button("Controls", self.controlsMenu)
        mainMenu.add.button("Settings", self.settingsMenu)
        mainMenu.add.button("Exit", pygame_menu.events.EXIT)
        logger.info("Main Menu Buttons created")
        
        mainMenu.mainloop(self.surface, self.drawBackground, fps_limit=FPS)

    def createPlayMenu(self):
        """creates the menu to select which level is going to be played

        Note:
            TODO Make columns rows dynamic with value of Levels

        Returns:
            Menu: contains the Play menu
        
        Test:
            * the score must be set with the help of the decorator
            * the size of this submenu must match WINDOWSIZE
            * clicking play on a existing level must start the gameloop
        """
        # pygame_menu makes screen scrollable if levels dont fit next to eachother
        playMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", columns=2, rows=3)
        
        decorator = playMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        playMenu.add.label(f"Level One")
        playMenu.add.image(self.levelOnePreview)
        playMenu.add.button(f"PLAY", self.game.gameLoop, self.player, self, 1)
        
        playMenu.add.label(f"Level Two")
        playMenu.add.image(self.comingSoon)
        playMenu.add.button(f"PLAY")
        
        logger.info(f"Play menu created")
        return playMenu
    
    def createCarMenu(self):
        """creates the menu to select and buy other cars

        Note:
            TODO column number generic with skin values
        
        Returns:
            Menu: contains the car menu
        
        Test:
            * After buying a car the select button must be shown
            * all labels, images and buttons must be set
        """
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
            carMenu.add.button("Select",self.player.setImage, BASICCAR_IMAGE)
        
        carMenu.add.image(self.price50)
        carMenu.add.image(self.copCar)
        # Hide "select" button to switch it easily with the buy button
        copSelectBut = carMenu.add.button("Select",self.player.setImage, COPCAR_IMAGE).hide()
        if(self.score["Cars"]["CopCar"] == True):
            copSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar,"CopCar", copSelectBut, COPCAR_IMAGE).add_self_to_kwargs(key="widget")
        
        carMenu.add.image(self.price100)
        carMenu.add.image(self.f1Car)
        f1SelectBut = carMenu.add.button("Select", self.player.setImage, F1_IMAGE).hide()
        if(self.score["Cars"]["F1Car"] == True):
            f1SelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "F1Car",f1SelectBut, F1_IMAGE).add_self_to_kwargs(key="widget")
        
        carMenu.add.image(self.price200)
        carMenu.add.image(self.sportsCar)
        sportsSelectBut = carMenu.add.button("Select",self.player.setImage, SPORTCAR_IMAGE).hide()
        if(self.score["Cars"]["SportsCar"] == True):
            sportsSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "SportsCar",sportsSelectBut, SPORTCAR_IMAGE).add_self_to_kwargs(key="widget")
        
        logger.info("Car Menu created")
        return carMenu
    
    def createSettingsMenu(self):
        """creates the settings menu
        
        Controls the music.
        
        Returns:
            Menu: contains the settings menu
        
        Test:
            * the pygame.mixer must stop playing if the value is off
            * the decorator for this menu must be in self.decorator list
        """
        settingsMenu = pygame_menu.Menu(width=WINDOWSIZE[0],height=WINDOWSIZE[1], theme=self.myTheme, title=" ", rows= 1, columns= 2)
        
        decorator = settingsMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        settingsMenu.add.label("Music")
        settingsMenu.add.toggle_switch(title="",infinite=True, state_text=("On", "Off"), state_values=(True, False) ,onchange=self.checkMusic)
        
        logger.info("settings menu created")
        return settingsMenu
    
    def checkMusic(self, state):
        """Checks the value of the switch and stops or resumes game music

        Args:
            state (Bool): True if the music should play, False otherwise
        
        Test:
            * music must stop if state == True
            * if the music is stopped it should not start if state == True
        """
        if state:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    
    
    def createControlsMenu(self):
        """creates the controls menu
        
        This menu is to look up the game controls

        Returns:
            Menu: contains the controls menu
        
        Test:
            * All Labels must be aligned left
            * the images must be in the same row as there label
        
        Examples:
            "Forward" must be in the same row as the image of self.wKey
        """
        
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
        """Draws backround image on the surface
        
        Test:
            * the background must be drawn on self.surface
            * background should not change after execution
        """
        self.background.draw(self.surface)
    
    def purchaseCar(self, car, purchBut, imagePath, widget):
        """logic for buying a new car

        Checks if the user has enough coins to buy a new car.
        If he can afford a new car his score is decreased and the select button is shown.
        Therfore the buy button is hidden.
        The newly bought car is automatically selected.
        
        Args:
            car (str): contains the name of the desired car
            purchBut (widget): contains the slect button that is still hidden
            widget (widget): contains the buy button that is shown 
            imagePath (str): path to the image of the desired car
        
        Test:
            * users score count cant get negative
            * if a car is purchased the buy button must be hiden and the select button needs to show on the screen
        """
        if(car == "CopCar" and PRICE_COPCAR <= self.score["Score"]):
            self.score["Cars"]["CopCar"] = True
            self.score["Score"] -= PRICE_COPCAR
            widget.hide()
            purchBut.show()
        elif(car == "F1Car" and PRICE_F1CAR <= self.score["Score"]):
            self.score["Cars"]["F1Car"] = True
            self.score["Score"] -= PRICE_F1CAR
            widget.hide()
            purchBut.show()
        elif(car == "SportsCar" and PRICE_SPORTSCAR <= self.score["Score"]):
            self.score["Cars"]["SportsCar"] = True
            self.score["Score"] -= PRICE_SPORTSCAR
            widget.hide()
            purchBut.show()
        else:
            if(car == "CopCar" or car == "F1Car" or car == "SportsCar"):
                logger.info("Something went wrong purchasing a car >> Price to high")
            else:
                logger.debug("Something went wrong purchasing a car >> car not found")
            return
        
        self.player.setImage(imagePath)
        self.updateScore()
        self.saveScore()
    
    def updateScore(self):
        """updates the score for every submenu with the help of the decorator list
        
        Test:
            * every decorator in the list needs to be called
            * the new text should not be on top of the old text
        """
        for dec in self.decorator:
            dec.remove_all()
            self.addScore(dec)
    
    def addScore(self, decorator):
        """draws the score and a coin on a given menu with the help of its decorator

        Args:
            decorator (decorator): decorator specific for a menu
        
        Test:
            * the text and image must be on the same hight
            * the changes should just be shown on the menu the decorator is binded to
        """
        decorator.add_text(y=SCORE_X, x=SCORE_TEXT_Y, text=str(self.score["Score"]), font=pygame_menu.font.FONT_8BIT, size=WIDGET_SIZE, color=BLACK)
        decorator.add_baseimage(y=SCORE_X, x=SCORE_COIN_Y, image=self.coin)
        logger.info(f"Updated Score to {self.score['Score']}")

    def setScore(self, value):
        """setter for score
        
        After completing a level successfully this function adds the reward to the score.

        Args:
            value (int): reward (coins) for finishing a level
        
        Test:
            * the score must increase
            * all menus must contain the new score (because updateScore is calles at the end)
        """
        self.score["Score"] += value 
        self.updateScore()
        self.saveScore()
    
    def loadScore(self):
        """loads the saved score and the purchased cars
        
        If no file is found a default value is taken.

        Returns:
            Dict: Contains the saved score and cars to enable / disable buttons
        
        Test:
            * check if file is found
            * if no file is found a default value must be taken
        """
        try:
            with open(SCORE_FILE, "rb") as f:
                savedScore = pickle.load(f)
        except:
            savedScore = {"Cars":{"BasicCar":True, "CopCar":False, "F1Car":False, "SportsCar":False}, "Score":0}
            logger.debug(f"Score File not found >> Default values used: {savedScore['Score']} , {savedScore['Cars']}")
        
        return savedScore    
    
    def saveScore(self):
        """saves the score into the file if the score changes
        
        If the File is not found a new file is created to save the score

        Test:
            * new value must be in given file after completion
            * logging file must contain information if file is not found
            * if no file is found a new file should be created
        """
        try:
            with open(SCORE_FILE, "wb") as f:
                pickle.dump(self.score, f)
            logger.info(f"Saved Information : {self.score['Score']} , {self.score['Cars']}")
        except:
            # Open in w+ mode to create automatically a new file
            with open(SCORE_FILE, "w+") as f:
                pass
            
            with open(SCORE_FILE, "wb") as f:
                pickle.dump(self.score, f)
            logger.debug(f"Saving new score failed, created a new File>> Check Path {SCORE_FILE}")