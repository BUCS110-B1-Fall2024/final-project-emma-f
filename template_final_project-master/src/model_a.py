class Cups:
    def __init__(self, x, y, color, imgfile=str):
        self.x = x #position of the cups
        self.y = y #position of the cups
        self.color = color # color of cups
        self.imgfile = imgfile 
        
class Cards:
    def __init__(self, x, y, color, number, imgfile=str):
        self.x = x
        self.y = y
        self.color = color
        self.number = number #card value
        self.imgfile = imgfile
        
class Deck:
    def __init__(self):
        return self