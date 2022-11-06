from pico2d import *


class Bullet:
    image = None
    def __init__(self, x =800, y=90, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('resource/aim/shoot_img/3.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):

        if self.velocity > 0:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'n', self.x, self.y, self.image.w//1.2, self.image.h//1.2)

        else:
           self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x, self.y, self.image.w//1.2, self.image.h//1.2)

    def update(self):
        self.x += self.velocity

    def get_bb(self): #충돌처리 값 받아주는 함수

        return self.x-10,self.y-10,self.x+10,self.y+10

