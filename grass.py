from pico2d import *

class Grass:
    def __init__(self,a,b):
        self.image = load_image('grass.png')
        self.x,self.y = a,b
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass
