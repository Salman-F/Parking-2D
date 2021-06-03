import pygame

from player import Player
from map import Map
from loguru import logger
from constants import *

class Game():
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
    
    def gameLoop(self, player, menu, level):
        player.setStart(STARTX, STARTY)
        
        if level == 1:
            map, background = self.loadMap(LVL1LAYOUT, LEVELONEBACKIMAGE)
            passedLevel = LEVEL1REWARD
            logger.info(f"Player started playing Level 1")
        elif level == 2:
            map, background = self.loadMap(LVL2LAYOUT, LEVELTWOBACKIMAGE)
            passedLevel = LEVEL2REWARD
            logger.info(f"Player started playing Level 2")
        else:
            logger.info(f"Level not found")
            return
        
        mainCar = pygame.sprite.GroupSingle()
        mainCar.add(player)
        
        done = False
        restart = False
        
        pauseBut = pygame.image.load(PAUSEBUTTON).convert_alpha()
        pauseBut = pygame.transform.scale(pauseBut, (PAUSEBUTTONW,PAUSEBUTTONH))
        pauseButRect = pauseBut.get_rect()
        pauseButRect.x = PAUSEBUTTONX
        pauseButRect.y = PAUSEBUTTONY
        
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
                player.setStart(STARTX, STARTY)
                done = False
                restart = False
                logger.info(f"Player restarted the current Level")
    
    def loadMap(self, layout, background):
        map = Map(layout)
        background = pygame.image.load(background)
        return map, background
    
    def showGameEnd(self, exitStatus):
        # Konstanten heraus schreiben
        tempSurface = self.createNewSurface()
        if exitStatus == 0:
            # Creating Game Over Text and aligning
            centeredText, centeredTextRect = self.createTextSurface("GAME OVER",RED, FONTSIZEGAME)
            centeredTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
            color = RED
        elif exitStatus == 1:
            # Creating You won Text and aligning
            centeredText, centeredTextRect = self.createTextSurface("YOU WON",GOLD, FONTSIZEGAME)
            centeredTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
            color = GOLD
        # Creating Press to continue text and aligning
        pressToCon, pressToConRect= self.createTextSurface("Press a key to continue", color, FONTSIZEGAME-10)
        pressToConRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 + FONTSIZEGAME)
        
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
        tempSurface = self.createNewSurface()
        
        restartText, restartTextRect = self.createTextSurface("Restart",RED, FONTSIZEGAME)
        exitText, exitTextRect = self.createTextSurface("Exit",RED, FONTSIZEGAME)
        
        restartTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2)
        exitTextRect.center = (WINDOWSIZE[0]/2, WINDOWSIZE[1]/2 + FONTSIZEGAME + PADDING)
        
        tempSurface.blit(restartText, restartTextRect)
        tempSurface.blit(exitText, exitTextRect)
        # To be able to unpause the game
        tempSurface.blit(pauseBut, pauseButRect)
        
        working = True
        while working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                if event.type == pygame.MOUSEBUTTONUP:
                        x, y = event.pos
                        if restartTextRect.collidepoint(x,y):
                            return True, True
                        if exitTextRect.collidepoint(x,y):
                            return True, False
                        if pauseButRect.collidepoint(x,y):
                            return False,False
            
            self.surface.blit(tempSurface, (0,0))
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def createTextSurface(self, text, color, size):
        font =  pygame.font.Font(FONT,size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        
        return textSurface, textRect
    
    def createNewSurface(self):
        tempSurface = pygame.Surface((WINDOWSIZE))
        whiteBack = pygame.image.load(WHITEBACKIMG).convert()
        tempSurface.blit(whiteBack, (0,0))
        tempSurface.set_alpha(2, pygame.RLEACCEL)
        return tempSurface