import pygame 
import pygame_menu
from loguru import logger
from pygame_menu.locals import ALIGN_LEFT
from pygame_menu.themes import Theme
from menuConstants import MenuConstants

class Menu():
    
    def __init__(self, savedScore):
        self.Const = MenuConstants()
        self.score = savedScore
        
        self.background = pygame_menu.BaseImage(image_path=self.Const.BACKIMAGE)
        self.coin = pygame_menu.BaseImage(image_path=self.Const.COINIMAGE).resize(width=40, height=40)
        self.wKey = pygame_menu.BaseImage(image_path=self.Const.WKEY).resize(width=50, height=50)
        self.sKey = pygame_menu.BaseImage(image_path=self.Const.SKEY).resize(width=50, height=50)
        self.dKey = pygame_menu.BaseImage(image_path=self.Const.DKEY).resize(width=50, height=50)
        self.aKey = pygame_menu.BaseImage(image_path=self.Const.AKEY).resize(width=50, height=50)
        self.hKey = pygame_menu.BaseImage(image_path=self.Const.HKEY).resize(width=50, height=50)
        self.spaceKey = pygame_menu.BaseImage(image_path=self.Const.SPACEKEY).resize(width=150, height=50)
        self.price50 = pygame_menu.BaseImage(image_path=self.Const.PRICE50).resize(width=120, height=50)
        self.price100 = pygame_menu.BaseImage(image_path=self.Const.PRICE100).resize(width=120, height=50)
        self.price200 = pygame_menu.BaseImage(image_path=self.Const.PRICE200).resize(width=120, height=50)

        self.basicCar = pygame_menu.BaseImage(image_path=self.Const.BASICCARIMAGE).resize(width=100, height=50).rotate(90)
        self.f1Car = pygame_menu.BaseImage(image_path=self.Const.F1IMAGE).resize(width=100, height=50).rotate(90)
        self.copCar = pygame_menu.BaseImage(image_path=self.Const.COPCARIMAGE).resize(width=100, height=50).rotate(90)
        self.sportsCar = pygame_menu.BaseImage(image_path=self.Const.SPORTCARIMAGE).resize(width=100, height=50).rotate(90)
        
        
        self.surface = pygame.display.set_mode(self.Const.WINDOW_SIZE)
        self.decorator = []
        pygame.display.set_caption("Parking 2D")
        # Creating own Theme
        self.myTheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.myTheme = Theme(
                                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                #Menu titel is not used | To get rid of warning that titel and background have same color
                                #TODO const here raus nehmen
                                title_font_color = (0, 0, 0),
                                widget_font_size = 33,  #CONST HERE TODO
                                widget_font = pygame_menu.font.FONT_8BIT,
                                widget_margin = (0,20), #CONST MARGIN HERE TODO
                            )
        self.myTheme.set_background_color_opacity(0.4) #CONST HERE TODO
        
        self.carMenu = self.createCarMenu()
        self.controlsMenu = self.createControlsMenu()
        self.playMenu = self.createPlayMenu()
        
        self.clock = pygame.time.Clock()
        logger.info("Menu initialized")
        
    def mainMenu(self, test):
        
        mainMenu = pygame_menu.Menu(width=self.Const.WINDOW_SIZE[0],height=self.Const.WINDOW_SIZE[1], theme=self.myTheme, title=" ", onclose=pygame_menu.events.EXIT)
        
        # Creating different buttons to press
        decorator = mainMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)

        mainMenu.add.button("Play",self.playMenu)
        mainMenu.add.button("Choose Car", self.carMenu)
        mainMenu.add.button("Controls", self.controlsMenu)
        mainMenu.add.button("Exit", pygame_menu.events.EXIT)
        logger.info("Main Menu Buttons created")
        
        
        while True:
            self.clock.tick(self.Const.FPS)

            mainMenu.mainloop(self.surface, self.drawBackground, disable_loop=test, fps_limit=self.Const.FPS)

            pygame.display.flip()
        
    def createPlayMenu(self):
        #TODO Make columns rows dynamic with value of Levels
        playMenu = pygame_menu.Menu(width=self.Const.WINDOW_SIZE[0],height=self.Const.WINDOW_SIZE[1], theme=self.myTheme, title=" ", columns=2, rows=3)
        
        decorator = playMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        
        playMenu.add.label(f"Level One")
        # TODO Real Pictures of the Level
        playMenu.add.image(self.basicCar)
        playMenu.add.button(f"PLAY")
        
        playMenu.add.label(f"Level Two")
        playMenu.add.image(self.sportsCar)
        playMenu.add.button(f"PLAY")
        
        return playMenu
    
    def createCarMenu(self):
        #
        #
        #TODO column number generic with skin values
        #TODO Honk for button select: set_sound button argument
        #TODO change price to text
        #TODO change skin of Player
        #
        myTheme = self.myTheme.copy()
        myTheme.widget_font_size = 22
        carMenu = pygame_menu.Menu(width=self.Const.WINDOW_SIZE[0],height=self.Const.WINDOW_SIZE[1], theme=myTheme, title=" ", columns=4, rows=3)
        
        decorator = carMenu.get_decorator()
        self.decorator.append(decorator)
        self.addScore(decorator)
        #TODO Padding ugly - think again. If there is no solution leave it
        carMenu.add.label(f"FREE").set_padding((20,0,15,0))

        carMenu.add.image(self.basicCar)
        if(self.score["Cars"]["BasicCar"] == True):
            carMenu.add.button("Select")
        
        #carMenu.add.label(f"Price {self.Const.PRICECOPCAR}")
        carMenu.add.image(self.price50)
        carMenu.add.image(self.copCar)
        # Hide "select" button to switch it easily with the buy button
        copSelectBut = carMenu.add.button("Select").hide()
        if(self.score["Cars"]["CopCar"] == True):
            copSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar,"CopCar", copSelectBut).add_self_to_kwargs(key="widget")
        
        #carMenu.add.label(f"Price {self.Const.PRICEF1CAR}")
        carMenu.add.image(self.price100)
        carMenu.add.image(self.f1Car)
        f1SelectBut = carMenu.add.button("Select").hide()
        if(self.score["Cars"]["F1Car"] == True):
            f1SelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "F1Car",f1SelectBut).add_self_to_kwargs(key="widget")
        
        #carMenu.add.label(f"Price {self.Const.PRICESPORTSCAR}")
        carMenu.add.image(self.price200)
        carMenu.add.image(self.sportsCar)
        sportsSelectBut = carMenu.add.button("Select").hide()
        if(self.score["Cars"]["SportsCar"] == True):
            sportsSelectBut.show()
        else:
            carMenu.add.button("Buy",self.purchaseCar, "SportsCar",sportsSelectBut).add_self_to_kwargs(key="widget")
        
        logger.info("Car Menu created")
        
        return carMenu
    
    def createControlsMenu(self):
        
        controlsMenu = pygame_menu.Menu(width=self.Const.WINDOW_SIZE[0],height=self.Const.WINDOW_SIZE[1], theme=self.myTheme, title=" ", columns=2, rows=6)
        
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
    
    def purchaseCar(self, car,purchBut, widget):
        if(car == "CopCar" and self.Const.PRICECOPCAR <= self.score["Score"]):
            self.score["Cars"]["CopCar"] = True
            self.score["Score"] -= self.Const.PRICECOPCAR
            widget.hide()
            purchBut.show()
        elif(car == "F1Car" and self.Const.PRICEF1CAR <= self.score["Score"]):
            self.score["Cars"]["F1Car"] = True
            self.score["Score"] -= self.Const.PRICEF1CAR
            widget.hide()
            purchBut.show()
        elif(car == "SportsCar" and self.Const.PRICESPORTSCAR <= self.score["Score"]):
            self.score["Cars"]["SportsCar"] = True
            self.score["Score"] -= self.Const.PRICESPORTSCAR
            widget.hide()
            purchBut.show()
        else:
            if(car == "CopCar" or car == "F1Car" or car == "SportsCar"):
                logger.info("Something went wrong purchasing a car >> Price to high")
            else:
                logger.debug("Something went wrong purchasing a car >> car not found")
        
        logger.info(f"{self.score['Score']} , {self.score['Cars']}")
        
        self.updateScore()
    
    def updateScore(self):
        for dec in self.decorator:
            dec.remove_all()
            self.addScore(dec)
    
    def addScore(self, decorator):
        #TODO BLACK CONSTANT
        #POS of text and image in const files
        decorator.add_text(y=-275, x=-300, text=str(self.score["Score"]), font=pygame_menu.font.FONT_8BIT, size=33, color=(0,0,0))
        decorator.add_baseimage(y=-275, x=-350, image=self.coin)
        logger.info("Updated Score")