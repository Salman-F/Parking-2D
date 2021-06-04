"""Constant file

This File contains all constants needed in the Code

    Attributes:
        name: SALFIC
        date: 03.06.2021
        version: 0.0.1
"""
import os

# WINDOW CONSTANTS
#######################
FPS = 60
WINDOWSIZE = (800,608)
LOG_FILE = os.path.join(os.path.dirname( __file__ ),".", "logging", "loggingInfos.log")

# MENU CONSTANTS
#######################
BACK_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "background.jpg")
WHITE_BACK_IMG = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "whiteBack.png")
COIN_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "coin.png")

PRICE_50 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-50-trans.png")
PRICE_100 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-100-trans.png")
PRICE_200 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-200-trans.png")

FONT = os.path.join(os.path.dirname( __file__ ),"..", "fonts", "retroFont.ttf")
PAUSE_BUTTON = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "pauseBut.png")

W_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "W-key.png")
S_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "S-key.png")
D_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "D-key.png")
A_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "A-key.png")
H_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "H-key.png")
SPACE_KEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "space-key.png")

COMING_SOON = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "coming-soon.png")
## Sound constant
HONK = os.path.join(os.path.dirname( __file__ ),"..", "sounds", "car-horn.mp3")
MUSIC = os.path.join(os.path.dirname( __file__ ),"..", "sounds", "music.wav")
## Constant fo saved score
SCORE_FILE = os.path.join(os.path.dirname( __file__ ),".", "score", "savedScore")

COIN_SIZE = 40
KEY_SIZE = 50

PRICE_W = 120
PRICE_H = 50

PREVIEW_W = 250
PREVIEW_H = 200

FONT_SIZE_GAME = 44
WIDGET_SIZE = 33
WIDGET_MARGIN = (0,20)
BACKGROUND_OPACITY = 0.4

PADDING = 20
SCORE_X = -285 # Position of Score display
SCORE_TEXT_Y = -320
SCORE_COIN_Y = -370

PAUSE_BUTTON_W = 40 # Position of pause button
PAUSE_BUTTON_H = 40
PAUSE_BUTTON_X = 740
PAUSE_BUTTON_Y = 20

MENU_CAR_W = 100
MENU_CAR_H = 50

PRICE_COPCAR = 50 # Prices to update player score
PRICE_F1CAR = 100
PRICE_SPORTSCAR = 200
PRICE_BASICCAR = 0

# Player Constant / Car Constant
#######################
BASICCAR_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "basic-car.png")
F1_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "f1-car.png")
COPCAR_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "police-car.png")
SPORTCAR_IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "sports-car.png")

START_X = 23
START_Y = 16
PIXEL_ALIGNMENT = 32
MAX_STEERING_ANGLE = 120
MAX_ACCELARATION = 10
MAX_VELOCITY = 60
DEACCELERATION = 2
REVERSE_ACCELERATION = 40
LENGTH = 4
STEERING_DIF = 60
PLAYER_WIDTH = 50
PLAYER_HIGHT = 100
PLAYER_INIT_ROT = 90

# Map Constant
#######################
SPRITE_FILE = os.path.join(os.path.dirname( __file__ ),"..", "images\maps", "customSpriteSheet.png")
## LEVEL 1
LVL1_LAYOUT = os.path.join(os.path.dirname( __file__ ),"..", "images\maps\LevelOne", "LVL1.csv")
LEVELONE_BACKIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\maps\LevelOne", "designLVL1.png")
LEVEL1_REWARD = 100
GOALL1_W = 6 # Size of goal * BLOCKSIZE
GOALL1_H = 12
## LEVEL 2
LVL2_LAYOUT = None
LEVELTWO_BACKIMAGE = None
LEVEL2_REWARD = 200

# Tile Constant
#######################
GOAL = "brown.png" # A single brown 16x16 block is used to position the top left corner of the goal while creating the map
BLOCK_SIZE = 16

# Colors
#######################
GOLD = (255,185,15)
RED = (255,0,0)
BLACK = (0,0,0)