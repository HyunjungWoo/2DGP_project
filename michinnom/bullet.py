from pico2d import *
import game_world
import math
direction = {'LEFT': -1, 'RIGHT':1 , 'UP':2, 'DOWN':0 }

class Bullet:
    def __init__(self,player):

        self.range = 0
        self.x = player.x + 15
        self.y = player.y + 3
        self.isOn = False
        self.image = load_image('resource/aim/shoot_img/3.png')
        self.dirx,self.diry = 0,0
        if player.direction == direction['RIGHT']:
            self.dirx = 1
            
        elif player.direction== direction['LEFT']:
            self.dirx = -1
            
        elif player.direction == direction['UP']:
            self.diry = 1
            self.x = player.x + 30
            self.y = player.y + 3
        elif player.direction == direction['DOWN']:
            self.diry = -1
    def update(self):
        if self.dirx != 0 and self.diry == 0:
            self.x += self.dirx* 20
        else:
            self.y += self.diry* 20
        
        if self.x < 0 or self.x > 1200 or self.y <0 or self.y >600:
            game_world.remove_object(self)
      

    def draw(self):
        if self.dirx == 1:
            self.image.draw(self.x,self.y,self.image.w,self.image.h)
        elif self.dirx == -1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x, self.y)
        elif self.diry == 1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, math.radians(270), 'h', self.x, self.y)
        elif self.diry == -1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, math.radians(90), 'h', self.x, self.y)
            
        