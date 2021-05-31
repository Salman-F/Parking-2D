import os

class MenuConstants():
    FPS = 60
    WINDOW_SIZE = (740,580)
    BACKIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "background.jpg")
    COINIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "coin.png")
    PRICE50 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-50-trans.png")
    PRICE100 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-100-trans.png")
    PRICE200 = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "Price-200-trans.png")
    
    WKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "W-key.png")
    SKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "S-key.png")
    DKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "D-key.png")
    AKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "A-key.png")
    HKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "H-key.png")
    SPACEKEY = os.path.join(os.path.dirname( __file__ ),"..", "images\menu", "space-key.png")
    
    BASICCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "basic-car.png")
    F1IMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "f1-car.png")
    COPCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "police-car.png")
    SPORTCARIMAGE = os.path.join(os.path.dirname( __file__ ),"..", "images\cars", "sports-car.png")
    PRICECOPCAR = 50
    PRICEF1CAR = 100
    PRICESPORTSCAR = 200
    PRICEBASICCAR = 0