class Character:
    def __init__(self, x=int, y=int, img_file=str):
        self.x = x
        self.y = y
        self.img_file = img_file
        
    def move_right(self):
        self.args = None
        return None
    
    def move_left(self):
        self.args = None
        return None
    
    def move_up(self):
        self.args = None
        return None
    
    def move_down(self):
        self.args = None
        return None
    
    def eating(self):
        return None
    
class Boy: 
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file
        
class Seed:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file
        