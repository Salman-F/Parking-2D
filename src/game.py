"""game
    
    Controls the gameloop and other UI elements while playing.
    
    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import pygame

from player import Player
from map import Map
from loguru import logger
from constants import *

class Game():
    """controls the gameloop and creates some user information screens
    """
    def __init__(self):
        """Creates a surface and starts pygame clock
        
        Test:
            * self.surface must be of type Surface
            * the clock must be contained in self.clock
        """
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
    
    def gameLoop(self, player, menu, level):
        """controls the gameloop
        
        Creates pause button to pause the game, restart, exit or turn the music on or off.
        Checks for userinput and calls specific funcitons at matching keys.
        Updates the surface and shows the user the updated view.

        Args:
            player (Player): contains the player to calls specific functions to move the player on surface
            menu (Menu): contains the last menu the user was on
            level (int): to determine which map to load and which background to plot on the surface
        
        Test:
            * the right map must be loaded based on the given level parameter
            * the pause button must be clickable
            * the rect of the goal must be drawn in gold
            * restarting the game should put the player on his start position
        """
        player.setStart(START_X, START_Y)
        
        if level == 1:
            map, background = self.loadMap(LVL1_LAYOUT, LEVELONE_BACKIMAGE)
            passedLevel = LEVEL1_REWARD
            logger.info(f"Player started playing Level 1")
        elif level == 2:
            map, background = self.loadMap(LVL2_LAYOUT, LEVELTWO_BACKIMAGE)
            passedLevel = LEVEL2_REWARD
            logger.info(f"Player started playing Level 2")
        else:
            logger.info(f"Level not found")
            return
        
        mainCar = pygame.sprite.GroupSingle()
        mainCar.add(player)
        
        done = False
        restart = False
        
        pauseBut = pygame.image.load(PAUSE_BUTTON).convert_alpha()
        pauseBut = pygame.transform.scale(pauseBut, (PAUSE_BUTTON_W,PAUSE_BUTTON_H))
        pauseButRect = pauseBut.get_rect()
        pauseButRect.x = PAUSE_BUTTON_X
        pauseButRect.y = PAUSE_BUTTON_Y
        
        while not done:
            dt = self.clock.get_time() / 1000
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.MOUSEBUTTONUP:
                        x, y = event.pos
                        if pauseButRect.collidepoint(x,y):
                            done, restart = self.pause(pauseBut,pauseButRect)
            
            pressed = pygame.key.get_pressed()
            
            # Controlling players acceleration
            if pressed[pygame.K_w]:
                player.forward(dt)
            elif pressed[pygame.K_s]:
                player.backward(dt)
            elif pressed[pygame.K_SPACE]:
                player.emergencyBrake()
            elif pressed[pygame.K_h]:
                player.honk()
            else:
                player.noAcceleration(dt)
            
            # Controlling player heading
            if pressed[pygame.K_d]:
                player.right(dt)
            elif pressed[pygame.K_a]:
                player.left(dt)
            else:
                player.straight()
            
            # cant use sprite group because sprite group doesnt allow return values
            gameOver, goal = player.update(dt, map.tiles, map.goal)
            
            if gameOver == True:
                done = True
                self.showGameEnd(0)
            elif goal == True:
                done = True
                self.showGameEnd(1)
                menu.setScore(passedLevel)
                
            # Drawing the tiles for precise collision detection
            map.drawMap(self.surface)
            # Plotting the design above
            self.surface.blit(background, (0,0))
            # Plotting the Goal rect
            pygame.draw.rect(self.surface, GOLD, map.goal.rect, 2)
            # Plotting the rotated image
            self.surface.blit(player.rotationImage, player.position * PIXEL_ALIGNMENT - (player.rect.width/2 , player.rect.height/2))
            # Plotting the pause button
            self.surface.blit(pauseBut, pauseButRect)
            
            pygame.display.flip()

            self.clock.tick_busy_loop(FPS)
        
            if restart == True:
                player.setStart(START_X, START_Y)
                done = False
                restart = False
                logger.info(f"Player restarted the current Level")
    
    def loadMap(self, layout, background):
        """loads map
        
        Initializes a map object that creates all tiles according to the given layout

        Args:
            layout (str): contains the path to the csv that is the base of our map
            background (str): contains the path to the matching png of the level

        Returns:
            map(Map): Contains the map object
            background(image): contains the loaded image
        
        Test:
            * the given background must be found and loaded
            * map must be of type Map
        """
        map = Map(layout)
        background = pygame.image.load(background)
        return map, background
    
    def showGameEnd(self, exitStatus):
        """shows game ending screen

        Args:
            exitStatus (int): decides if a "game over" screen or "you won" screen is shown. Contains the reason of the stopped game.
        
        Test:
            * is the text aligned correctly
            * the screen should not close if a button was held down while playing and released after this screen shows up
                Just newly pressed keys should be detected
        """
        # Konstanten heraus schreiben
        tempSurface = self.createNewSurface()
        if exitStatus == 0:
            # Creating Game Over Text and aligning
            centeredText, centeredTextRect = self.createTextSurface("GAME OVER",RED, FONT_SIZE_GAME)
            centeredTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
            color = RED
        elif exitStatus == 1:
            # Creating You won Text and aligning
            centeredText, centeredTextRect = self.createTextSurface("YOU WON",GOLD, FONT_SIZE_GAME)
            centeredTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
            color = GOLD
        # Creating Press to continue text and aligning
        pressToCon, pressToConRect= self.createTextSurface("Press a key to continue", color, FONT_SIZE_GAME-10)
        pressToConRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 + FONT_SIZE_GAME)
        
        tempSurface.blit(centeredText, centeredTextRect)
        tempSurface.blit(pressToCon, pressToConRect)
        
        working = True
        newlyPressed = False
        while working:
            # Waiting fo a key press
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        working = False
                    if event.type == pygame.KEYDOWN:
                        newlyPressed = True
                    if event.type == pygame.KEYUP and newlyPressed:
                        working = False
            
            self.surface.blit(tempSurface, (0,0))
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def pause(self, pauseBut, pauseButRect):
        """creates a pause menu for the player

        Args:
            pauseBut (image): contains the loaded image to display on the surface
            pauseButRect (Rect): contains the position of the image

        Returns:
            restart (Bool): True if the game should be restarted, False otherwise
            done (Bool): True if the game is exited or restarted, False otherwise
        
        Test:
            * the pause button must be clickable again to unpause
            * text should not overlap other text
        """
        tempSurface = self.createNewSurface()
        
        unpauseText, unpauseRect = self.createTextSurface("Unpause", RED, FONT_SIZE_GAME)
        restartText, restartTextRect = self.createTextSurface("Restart",RED, FONT_SIZE_GAME)
        musicSwitchText, musicSwitchTextRect = self.createTextSurface("Music On/Off", RED, FONT_SIZE_GAME)
        exitText, exitTextRect = self.createTextSurface("Exit",RED, FONT_SIZE_GAME)
        
        unpauseRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 - FONT_SIZE_GAME - PADDING)
        restartTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
        musicSwitchTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 + FONT_SIZE_GAME + PADDING)
        exitTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 + 2 * FONT_SIZE_GAME + 2* PADDING)
        
        tempSurface.blit(unpauseText, unpauseRect)
        tempSurface.blit(restartText, restartTextRect)
        tempSurface.blit(musicSwitchText, musicSwitchTextRect)
        tempSurface.blit(exitText, exitTextRect)
        
        # To be able to unpause the game
        tempSurface.blit(pauseBut, pauseButRect)
        restart = False
        done = False
        working = True
        while working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                if event.type == pygame.MOUSEBUTTONUP:
                        x, y = event.pos
                        # Checks for collision between the mouse and the rects of the text
                        if restartTextRect.collidepoint(x,y):
                            restart, done = True, True
                            return restart, done
                        if exitTextRect.collidepoint(x,y):
                            restart, done = True, False
                            return restart, done
                        if pauseButRect.collidepoint(x,y) or unpauseRect.collidepoint(x,y):
                            restart, done = False, False
                            return restart, done
                        if musicSwitchTextRect.collidepoint(x,y):
                            musicBusy = pygame.mixer.music.get_busy()
                            if musicBusy:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
            
            self.surface.blit(tempSurface, (0,0))
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def createTextSurface(self, text, color, size):
        """helper function to create a text surface

        Args:
            text (str): contains the specific text that should be shown
            color (tupel): RGB tupel for coloring the text
            size (int): size of the text

        Returns:
            textSurface (Surface): contains the created surface with the rendet text
            textRect (Rect): rect of the textSurface
        
        Test:
            * the decleared font must be used
            * text must be in given color
        """
        font =  pygame.font.Font(FONT,size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        
        return textSurface, textRect
    
    def createNewSurface(self):
        """helper function to create a pause menu or game end screen

        Returns:
            Surface: contains a new surface with white background
        
        Test:
            * the whitebackground must be a little seethrough
            * the new surface must be the same size as WINDOWSIZE
        """
        tempSurface = pygame.Surface((WINDOWSIZE))
        whiteBack = pygame.image.load(WHITE_BACK_IMG).convert()
        tempSurface.blit(whiteBack, (0,0))
        tempSurface.set_alpha(2, pygame.RLEACCEL)
        return tempSurface