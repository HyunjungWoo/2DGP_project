from pico2d import *
import play_state
import game_world
from boss import Boss_Goopy
direction = {'LEFT': -1, 'RIGHT':1 , 'UP':2, 'DOWN':0 }

class Bullet:
    image = None
    def __init__(self,player):
        self.sort = 'bullet'
        self.range = 0
        self.x = player.x + 25
        self.y = player.y + 20
        self.isOn = False
        if Bullet.image == None:
            Bullet.image = load_image('resource/aim/shoot_img/3.png')
        self.dirx,self.diry = 0,0
        if player.direction == direction['RIGHT']:
            self.dirx = 1
        elif player.direction== direction['LEFT']:
            self.dirx = -1
        elif player.direction == direction['UP']:
            self.diry = 1
            self.x = player.x + 32
            self.y = player.y + 5
        elif player.direction == direction['DOWN']:
            self.diry = -1
    def update(self):

        if self.dirx != 0 and self.diry == 0:
            self.x += self.dirx * 20
        else:
            self.y += self.diry * 20

        if self.x < 0 or self.x > 1200 or self.y <0 or self.y > 600:
            game_world.remove_object(self)
    
    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.dirx == 1:
             self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'n', self.x,self.y,self.image.w/1.2, self.image.h/1.2)
        elif self.dirx == -1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x,self.y,self.image.w/1.2, self.image.h/1.2)
        elif self.diry == 1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, math.radians(270), 'h', self.x,self.y,self.image.w/1.2, self.image.h/1.2)
        elif self.diry == -1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, math.radians(90), 'h', self.x,self.y,self.image.w/1.2, self.image.h/1.2)
            
    def get_bb(self): 
        if self.diry == 1 :#위쪽
            return self.x-10,self.y-50,self.x+10,self.y+50
        else:
            return self.x-50,self.y-13,self.x+50,self.y+13  #왼쪽,왼쪽바닥,오른쪽 , 오른쪽 바닥 
    def handle_collision(self,other,group):
        if other.sort == 'monster':
            other.hp -= 10
            game_world.remove_object(self)
            
        
