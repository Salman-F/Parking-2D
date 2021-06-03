import os

FPS = 60
WINDOWSIZE = (800,608)
BACKIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "background.jpg")
WHITEBACKIMG = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "whiteBack.png")
COINIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "coin.png")
PRICE50 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-50-trans.png")
PRICE100 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-100-trans.png")
PRICE200 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-200-trans.png")
FONT = os.path.join(os.path.dirname( __file__ ),"..", "fonts\karmatic-arcade", "ka1.ttf")
PAUSEBUTTON = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "pauseBut.png")

SCOREFILE = os.path.join(os.path.dirname( __file__ ),".", "score", "savedScore")
LOGFILE = os.path.join(os.path.dirname( __file__ ),".", "logging", "loggingInfos.log")
STARTX = 23
STARTY = 16

SPRITEFILE = os.path.join(os.path.dirname( __file__ ),"..", "images\maps", "customSpriteSheet.png")
LVL1LAYOUT = os.path.join(os.path.dirname( __file__ ),"..", "images\maps\LevelOne", "LVL1.csv")
LEVELONEBACKIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\maps\LevelOne", "designLVL1.png")
LEVEL1REWARD = 100
GOAL = "brown.png"
LVL2LAYOUT = None
LEVELTWOBACKIMAGE = None
LEVEL2REWARD = 200

GOLD = (255,185,15)
RED = (255,0,0)
BLACK = (0,0,0)

FONTSIZEGAME = 44
WIDGET_SIZE = 33
WIDGET_MARGIN = (0,20)
BACKGROUND_OPACITY = 0.4
PADDING = 4
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
SCORE_X = -285
SCORE_TEXT_Y = -320
SCORE_COIN_Y = -370

COIN_SIZE = 40
KEY_SIZE = 50
PRICE_W = 120
PRICE_H = 50

PAUSEBUTTONW = 40
PAUSEBUTTONH = 40
PAUSEBUTTONX = 740
PAUSEBUTTONY = 20
MENU_CAR_W = 100
MENU_CAR_H = 50

GOALL1W = 6
GOALL1H = 12

WKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "W-key.png")
SKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "S-key.png")
DKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "D-key.png")
AKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "A-key.png")
HKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "H-key.png")
SPACEKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "space-key.png")
HONK = os.path.join(os.path.dirname( __file__ ),"..", "sounds", "car-horn.mp3")

BASICCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "basic-car.png")
F1IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "f1-car.png")
COPCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "police-car.png")
SPORTCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "sports-car.png")
PRICECOPCAR = 50
PRICEF1CAR = 100
PRICESPORTSCAR = 200
PRICEBASICCAR = 0

BLOCK_SIZE = 16