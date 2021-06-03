"""Player class

    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""

import pygame

from pygame import Vector2
from loguru import logger
from math import sin, radians, degrees, copysign
from constants import *

class Player(pygame.sprite.Sprite):
    """Handels player activities

    Args:
        pygame (Sprite): Inherits from pygame Sprite class

    """
    def __init__(self, imagePath, x, y):
        """Creates object of player class

        Note:
            The formula for the physics and as a guidens this source was used:
                - https://rmgi.blog/pygame-2d-car-tutorial.html
        
        Args:
            imagePath (str): contains the path to the default car image
            x (int): contains starting x position
            y (int): contains starting y position
        
        Test:
            * start position must be (x,y)
            * deafult image must be set
        """
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
        """Accelerates the player backward
        
        Checks if the car is moving forward or backwards and acts apropiat
            
        Args:
            timeDif (float): contains the time since last frame
        
        Test:
            * acceleration must stay between maxAcceleration and -maxAcceleration
            * the acceleration must increace if velocity.y > 0
        """
        if self.velocity.y < 0:
            self.acceleration = self.reverseAcceleartion
        else:
            self.acceleration += 1 * timeDif
            
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)

    def forward(self, timeDif):
        """Accelerates the player forward
        
        Checks if the car is moving forward or backwards and acts apropiat

        Args:
            timeDif (float): contains the time since last frame
            
        Test:
            * acceleration must stay between maxAcceleration and -maxAcceleration
            * the acceleration must decrease if velocity.y < 0
        """
        if self.velocity.y > 0:
            self.acceleration = -self.reverseAcceleartion
        else:
            self.acceleration -= 1 * timeDif
        
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)
    
    def emergencyBrake(self):
        """Stops the car immediately
        
        Test:
            * velocity.y must be 0 at the end
            * did the function change other variables
        """
        self.velocity.y = 0
    
    def noAcceleration(self, timeDif):
        """Slowly decreases the speed of the car
        
        After a decleared value is reached the car is fully stopped to prevent slowly creeping of the car

        Args:
            timeDif (float): contains the time since last frame
        
        Test:
            * the car must be fully stopped after reaching the defined limit
            * the acceleration must have the opposite sign as velocity.y if the defined limit is not reached
        """
        if abs(self.velocity.y) > timeDif * self.deaccelaration:
            self.acceleration = -copysign(self.deaccelaration, self.velocity.y)
        else:
            self.velocity.y = 0
            self.acceleration = 0
        
        self.acceleration = self.checkLimits(self.acceleration, self.maxAcceleration)
    
    def right(self, timeDif):
        """Increases the steering of the car
        
        Args:
            timeDif (float): contains the time since last frame
            
        Test:
            * the steering must be increased by STEERING_DIF (declared in constants.py)
            * the steering must be lower or equal maxSteering
        """
        self.steering += STEERING_DIF * timeDif
        self.steering = self.checkLimits(self.steering, self.maxSteering)
    
    def left(self, timeDif):
        """Decreases the steering of the car
        
        Args:
            timeDif (float): contains the time since last frame
            
        Test:
            * the steering must be decreased by STEERING_DIF (declared in constants.py)
            * the steering must be greater or equal then -maxSteering
        """
        self.steering -= STEERING_DIF * timeDif
        self.steering = self.checkLimits(self.steering, self.maxSteering)
        
    def straight(self):
        """Neutralizes the steering
        
        Test:
            * the steering must be 0 at the end of the function
            * other variables should not be changed
        """
        self.steering = 0
    
    def honk(self):
        """Plays a honk noise
        
        Test:
            * the noise has to be played
            * pygame.mixer needs to be initialized
        """
        self.honkNoise.play()
    
    def checkLimits(self, value, maxValue):
        """Checks if a given value exceeds its given maxValue
        
        Is the given maxValue is reached or exceeded, the given value is set to this maxValue

        Args:
            value (float): specific value of a variable
            maxValue (int): maxvalue of this variable

        Returns:
            Float: Checked value
        
        Test:
            * return value can not be greater or less then max or -maxValue
            * if the value did not exceed- or is not equal to maxValue the returned value should be the same as the given one
        """
        if value >= maxValue:
            value = maxValue
        elif value <= -maxValue:
            value = -maxValue
            
        return value

    def calcTurning(self):
        """Calculates the turning with given formula
        
        Based on this calculation the angle of rotation is calculated.
        Therfore the given image can be rotated.

        Returns:
            Float: Contains the velocity while turning
        
        Test:
            * if steering equals to zero no calculation should be made
            * the turningvelocity must be 0 if the steering is neutral
        """
        turningVelocity = 0
        
        if self.steering:
            turningRadius = self.length / sin(radians(self.steering))
            turningVelocity = self.velocity.y / turningRadius
        else:
            turningVelocity = 0
        
        return turningVelocity
    
    def collisionDetection(self, tiles):
        """Checks for collision between the car and obstacles
        
        Based on masks the player class and the tiles class have

        Args:
            tiles (list): contains all tiles that represant an obstacle

        Returns:
            Bool: True if the player coordinates match one of the tiles coordinates, False otherwise
        
        Test:
            * logging information must be writen in log file
            * hit must be True if the player collides with an obstacle
        """
        hit = False
        if pygame.sprite.spritecollide(self, tiles, False, pygame.sprite.collide_mask):
            hit = True
            logger.info(f"Player hit something!")
        return hit
    
    def checkGoalReach(self, goal):
        """Checks if the player rect is inside of the goal rect

        Args:
            goal (Tile): contains the information and rect of the goal

        Returns:
            Bool: True if the rect of player is inside of the rect of goal, False otherwise
        
        Test:
            * logging information must be in log file
            * true must be returned if player is in the goal
        """
        goal = False
        if pygame.Rect.contains(goal.rect, self.rect):
            logger.info(f"Player reached the goal")
            goal = True
            
        return goal
    
    def update(self, timeDif, tiles, goal):
        """Updates the parameters of the player
        
        Increases / Decreases the velocity, position and angle.
        Rotates the image based on the changed variables.
        Calls collision functions to check for collisions.

        Args:
            timeDif (float): contains the time since last frame
            tiles (list): contains all tiles that represant an obstacle
            goal (Tile): contains the information and rect of the goal

        Returns:
            hit(Bool): True if a hit occured, False otherwise
            goal(Bool): True if the player is in the goal, False otherwise
        
        Test:
            * if a angle is equal to zero the image can not rotate
            * velocity, position and angle must changed if the user pressed a valid key
        """
        
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
        
        hit = self.collisionDetection(tiles)
        goal = self.checkGoalReach(goal)

        return hit, goal
    
    def setImage(self, imagePath):
        """Setter for the image of the player

        Args:
            imagePath (str): Contains the path to the desired image
        
        Test:
            * the imagePath must be valid
            * the image must be (changed) the same as found in imagePath
        """
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.rotate(self.image, PLAYER_INIT_ROT)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HIGHT))
        logger.info(f"Car Image set to {imagePath}")
    
    def setStart(self, x, y):
        """Sets the variables of the player
        
        Is mostly used for restarting the game through the pause menu

        Args:
            x (int): contains the x position
            y (int): contains the y position
        
        Test:
            * the center of the rect must be at the given x, y values
            * all variables must be zero
        """
        # At Game Restart all variables will return to their start state
        self.rect.centerx = x * PIXEL_ALIGNMENT
        self.rect.centery = y * PIXEL_ALIGNMENT
        self.position = Vector2(x,y)
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.steering = 0.0
        self.angle = 0.0