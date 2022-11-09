from pico2d import *

state = {'STAY': 0, 'RUNNING' : 1,'JUMPING':2,'Aim' : 3,'Paring':4}
direction = {'LEFT': 0, 'RIGHT':1 }
bullets = []
bulletCount = 0
class Bullet:
    def __init__(self, CupHead):
        self.range = 0
        self.x = CupHead.x
        self.y = CupHead.y
        self.isOn = False
        self.image = load_image('resource/aim/shoot_img/3.png')
        self.dir = 1
        if CupHead.direction == direction['RIGHT']:
            self.dir = 1
            self.range = CupHead.x + 600  #사거리
        elif CupHead.direction == direction['LEFT']:
            self.dir = -1
            self.range = CupHead.x - 600

    def update(self):
        global bulletCount
        self.x += self.dir * 50

        if not len(bullets) == 0:
            if self.dir == 1:
                if self.x >= self.range:
                    bullets.remove(self)
            elif self.dir == -1:
                if self.x <= self.range:
                    bullets.remove(self)


    def draw(self):
        if self.dir == 1:
            self.image.draw(self.x,self.y,self.image.w,self.image.h)
        elif self.dir == -1:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x, self.y)


class CupHead:
    def __init__(self):

        self.x, self.y = 400, 90
        self.stay_frame = 1
        self.run_frame = 0
        self.jump_frame = 0
        self.aim_frame = 1
        self.paring_frame = 1
        self.image = load_image('stay.png')
        self.state = state['STAY']
        self.direction = direction['RIGHT']
        self.jumpSpeed = 0
        self.dirx = 0
        self.mass = 2 # 무게
        self.parring_img = load_image('resource/aim/shoot_img/shooting1.png')

    def makeBullets(self):
        bullets.append(Bullet(self))

    def deleteBullets(self):
        bullets.remove(Bullet(self))
    def update(self):
        if (self.state == state['RUNNING']):
            self.image = load_image('run_right.png') #오른쪽으로 달리고 있는 이미지
            self.run_frame = (self.run_frame +1) % 16

#
        elif(self.state == state['STAY']):
            if self.stay_frame == 6:
                self.stay_frame = 1
            self.image = load_image('resource/idle/idle(%d).png' % (self.stay_frame))
            self.stay_frame = (self.stay_frame + 1) % 5
            self.stay_frame += 1

        elif (self.state == state['Aim']):
            if self.aim_frame == 6:
                self.aim_frame = 1
            self.image = load_image('resource/aim/Straight/cuphead_aim_straight_000%d.png' % (self.aim_frame))
            self.aim_frame = (self.aim_frame + 1) % 5
            self.aim_frame += 1

        elif(self.state == state['Paring']):
            if self.paring_frame == 8:
                self.paring_frame = 1
            self.image = load_image('resource/aim/special_attack/Straight/Ground/paring(%d).png' % (self.paring_frame)) #캐릭터 발사모션
            self.parring_img = load_image('resource/aim/shoot_img/shooting_%d.png' % (self.paring_frame)) # 슈팅이미지
            self.paring_frame = (self.paring_frame + 1) % 7
            self.paring_frame += 1


        elif(self.state == state['JUMPING']):

            self.image = load_image('jumping.png')
            self.jump_frame = (self.jump_frame +1) % 8



            if self.jumpSpeed > 0:
                 F = (0.5 * self.mass * (self.jumpSpeed **2))
            else:
                 F = -(0.5 * self.mass * (self.jumpSpeed **2))

          
            self.y += round(F)
            self.jumpSpeed -= 1

            if self.y < 90:
                self.y = 90
                self.state = state['STAY']
                self.jumpSpeed = 8

        self.x = self.x + self.dirx * 7.5
        for bullet in bullets:
            bullet.update()


    def draw(self):
        if (self.state == state['Aim']):
            if (self.direction == direction['RIGHT']):

                self.image.clip_composite_draw(0,0,self.image.w ,self.image.h,0,'n',self.x,self.y)

                delay(0.02)
            elif(self.direction == direction['LEFT']):

                self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x, self.y)
                delay(0.02)

        if (self.state == state['Paring']):
            if (self.direction == direction['RIGHT']):

                self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'n', self.x, self.y,self.image.w, self.image.h)
                self.parring_img.clip_composite_draw(0, 0, self.parring_img.w, self.parring_img.h, 0, 'n', self.x + 100, self.y)


            elif (self.direction == direction['LEFT']):
                pass


        if (self.state == state['STAY']):
            if (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(0,0, self.image.w, self.image.h, 0, 'h',  self.x, self.y)

            elif(self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(0,0, self.image.w, self.image.h, 0, 'n',  self.x, self.y)

        if (self.state == state['RUNNING']):
            if (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(self.run_frame * 190, 0,190, 239, 0,'h',self.x, self.y,190,239) ## 달리기 오른쪽으로 #달리기 이미지

            elif(self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(self.run_frame * 190, 0,190, 239, 0,'n',self.x, self.y,190,239)

        if (self.state == state['JUMPING']):
            if (self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(self.jump_frame * 151, 0, 151, 179, 0, 'n', self.x, self.y, 151, 179)

            elif (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(self.jump_frame * 151, 0, 151, 179, 0, 'h', self.x, self.y, 151, 179)


        for bullet in bullets:
            bullet.draw()
class Potato_Monster:
    def __init__(self):
        self.frame = 0
        self.sin = 5
        self.image = load_image('potato.png')
        self.ddong = load_image('ddong.png')
        self.attack = load_image('potato_attack.png')
        self.print = 0
        self.x,self.y = 750,300
    def update(self):
        self.frame = (self.frame + 1) % self.sin

    def draw(self):
        #self.appear_motion()

        self.attack_draw()
        if(self.print >= 12):
            self.ddong_draw()
            
    def appear_motion(self):
        pass
    def ddong_draw(self):

        self.x -= 100
        self.ddong.clip_draw(self.frame * 134, 1,133,138,self.x,100)
    def attack_draw(self):
        self.sin = 12
        self.attack.clip_draw(self.frame * 542, 0, 542, 590, 880, self.y)
        self.print += 1
