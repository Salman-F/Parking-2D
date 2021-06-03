import pygame

from pygame import Vector2
from loguru import logger
from math import sin, radians, degrees, copysign
from constants import *

class Player(pygame.sprite.Sprite):
    #Physicy and everythin inspired from https://rmgi.blog/pygame-2d-car-tutorial.html
    def __init__(self, imagePath, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.setImage(imagePath)
        self.rect = self.image.get_rect()
        # Initialiazing of important variables
        self.setStart(x,y)
        #Initialize some max values
        self.length = LENGTH
        self.maxSteering = MAX_STEERING_ANGLE
        self.maxAcceleration = MAX_ACCELARATION
        self.maxVelocity = MAX_VELOCITY
        #Variables for smooth stopping
        self.deaccelaration = DEACCELERATION
        self.reverseAcceleartion = REVERSE_ACCELERATION

        self.honkNoise = pygame.mixer.Sound(HONK)
    
    def backward(self, timeDif):
        if self.velocity.y < 0:
            self.acceleration = self.reverseAcceleartion
        else:
            self.acceleration += 1 * timeDif
            
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)

    def forward(self, timeDif):
        if self.velocity.y > 0:
            self.acceleration = -self.reverseAcceleartion
        else:
            self.acceleration -= 1 * timeDif
        
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)
    
    def emergencyBrake(self):
        self.velocity.y = 0
    
    def noAcceleration(self, timeDif):
        if abs(self.velocity.y) > timeDif * self.deaccelaration:
            self.acceleration = -copysign(self.deaccelaration, self.velocity.y)
        else:
            self.velocity.y = 0
            self.acceleration = 0
        
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)
    
    def right(self, timeDif):
        self.steering += STEERING_DIF * timeDif
        self.steering = self.checkLimits(self.steering, self.maxSteering)
    
    def left(self, timeDif):
        self.steering -= STEERING_DIF * timeDif
        self.steering = self.checkLimits(self.steering, self.maxSteering)
        
    def straight(self):
        self.steering = 0
    
    def honk(self):
        self.honkNoise.play()
    
    def checkLimits(self, value, maxValue):
        if value >= maxValue:
            value = maxValue
        elif value <= -maxValue:
            value = -maxValue
            
        return value

    def calcTurning(self):
        turningVelocity = 0
        
        if self.steering:
            turningRadius = self.length / sin(radians(self.steering))
            turningVelocity = self.velocity.y / turningRadius
        else:
            turningVelocity = 0
        
        return turningVelocity
    
    def collisionDetection(self, tiles):
        hit = False
        if pygame.sprite.spritecollide(self, tiles, False, pygame.sprite.collide_mask):
            hit = True
            logger.info(f"Player hit something!")
        return hit
    
    def checkGoalReach(self, goal):
        if pygame.Rect.contains(goal.rect, self.rect):
            logger.info(f"Player reached the goal")
            return True
    
    def update(self, timeDif, tiles, goal):
        
        # Increasing / decreasing the velocity
        self.velocity += (0, self.acceleration * timeDif)
        self.velocity.y = self.checkLimits(self.velocity.y, self.maxVelocity)
        
        #Calculating turning radius and velocity
        turningVelocity = self.calcTurning()

        self.position += self.velocity.rotate(-self.angle) * timeDif
        self.angle += degrees(turningVelocity) * timeDif

        self.rotationImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotationImage.get_rect()
        
        self.rect.centerx = self.position.x * PIXEL_ALIGNMENT 
        self.rect.centery = self.position.y * PIXEL_ALIGNMENT
        # Updating the mask for upcoming collision detection
        self.mask = pygame.mask.from_surface(self.rotationImage)
        
        #hit = self.collisionDetection(tiles)
        #goal = self.checkGoalReach(goal)
        hit, goal = False, False
        return hit, goal
    
    def setImage(self, imagePath):
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.rotate(self.image, PLAYER_INIT_ROT)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HIGHT))
        logger.info(f"Image set to {imagePath}")
    
    def setStart(self, x, y):
        # At Game Restart all variables will return to their start state
        self.rect.centerx = x * PIXEL_ALIGNMENT
        self.rect.centery = y * PIXEL_ALIGNMENT
        self.position = Vector2(x,y)
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.steering = 0.0
        self.angle = 0.0