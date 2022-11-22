from pico2d import *
import game_framework

state = { 'JUMP_F':0, 'Punch':1 , 'Die':2 , 'JUMP_D':3, 'JUMP_U':4, 'Morph':5}
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH  = 30.0  # Km / Hour
RUN_SPEED_MPM   = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS   = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS   = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
JUMP_TIME_PER_ACTION   = 1.0 #속도 조절
JUMP_ACTION_PER_TIME   = 1.0 / JUMP_TIME_PER_ACTION

JUMP_F_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
JUMP_F_TIME_PER_ACTION   = 5.0 #속도 조절
JUMP_F_ACTION_PER_TIME   = 1.0 / JUMP_TIME_PER_ACTION

PUNCH_FRAMES_PER_ACTION = 16 # 프레임 장수(사진 갯수)
PUNCH_TIME_PER_ACTION   = 2.5 #속도 조절
PUNCH_ACTION_PER_TIME   = 1.0 / PUNCH_TIME_PER_ACTION

MORPH_FRAMES_PER_ACTION = 42 # 프레임 장수(사진 갯수)
MORPH_TIME_PER_ACTION   = 10 #속도 조절
MORPH_ACTION_PER_TIME   = 1.0 / MORPH_TIME_PER_ACTION
px,py= 0,0
class Boss_Goopy:
    jump_F =[]
    Punch = []
    jump_D = []
    jump_U = []
    Morph = []
    def __init__(self):
        self.state = state['JUMP_F']
        self.hp = 1400 
        self.image = None
        self.x,self.y = 780, 100
        self.dir = 1 #오른쪽 
        self.dirx, self.diry = 0, 0
        self.frame = 0
        self.jumpcount = 0
        self.timer = 0
        self.jumpheight, self.mass= 4, 1
        self.sort = 'monster'
        self.punchcount = 0
        self.phase = 1  # 페이즈 1 
        for i in range(9): #jump_F 제자리점프  이미지 리소스
            a = load_image('monster/Goopy/Phase 1/Jump/slime_jump_%d.png' % i)
            Boss_Goopy.jump_F.append(a)
        for i in range(3): #jump_D 아래로 떨어지는 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Air Down/air_down(%d).png' % i)
            Boss_Goopy.jump_D.append(a)
        for i in range(3):#jump_U 위로 올라가는 이미지 리소스
            a = load_image('monster/Goopy/Phase 1/Air UP/air_up(%d).png' % i)
            Boss_Goopy.jump_U.append(a)
        for i in range(16):#punch 펀치 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Punch/slime_punch(%d).png' % i)
            Boss_Goopy.Punch.append(a)
        for i in range(44):#morph 2페이즈 변신 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Transition To ph2/slime_morph(%d).png' % i)
            Boss_Goopy.Morph.append(a)
    def get_bb(self):
            return self.x-50,self.y-50,self.x+50,self.y+50 
    def update(self):
        if self.hp < 1000 and self.y <=100:
            self.phase = 2
            self.jumpcount = 4
            

        if self.jumpcount <3:
            jump(self)
        else:
            if self.phase == 1:
                self.state = state['Punch']
            elif self.phase == 2:
                self.state = state['Morph']

        if self.state == state['JUMP_F']:
            jump_F_update(self)
        elif self.state == state['Punch']:
            punch_update(self)
        elif self.state == state['JUMP_D']:
            jump_D_update(self)
        elif self.state == state['JUMP_U']:
            jump_U_update(self)  
        elif self.state == state['Morph']:
            morph_update(self)                   

    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.state == state['Punch']:
            if self.dir == 1:
                punch_draw_right(self)
            else:
                punch_draw_left(self)
        elif self.state == state['JUMP_F']:
            jump_F_draw(self)
        elif self.state == state['JUMP_D']:
            jump_D_draw(self)
        elif self.state == state['JUMP_U']:
            jump_U_draw(self)
        elif self.state == state['Morph']:
            morph_draw(self)
    def handle_collision(self,other,group):
        pass



def morph_update(self):
    self.frame  = (self.frame + MORPH_FRAMES_PER_ACTION * MORPH_ACTION_PER_TIME * game_framework.frame_time) % 42
    print(self.frame)

def morph_draw(self):
    global px,py
    if int(self.frame) == 0: px,py = 0,0
    elif int(self.frame) == 1:  px,py  = -20,0 
    elif int(self.frame) == 2:  px,py  = -30,5
    elif int(self.frame) == 3:  px,py  = -40,5
    elif int(self.frame) == 4:  px,py  = -50,5
    elif 5<=int(self.frame)<9:  px,py  = -50,0
    elif int(self.frame) == 9:  px,py  = -50,40
    elif int(self.frame) == 10: px,py = -50,85
    elif int(self.frame) == 11: px,py = -50,110
    elif 11<int(self.frame)<17: px,py = -50,120
    elif int(self.frame) == 17: px,py = -50,110
    elif int(self.frame) == 18: px,py = -50,85
    elif int(self.frame) == 19: px,py = -50,45
    elif int(self.frame) == 20: px,py = -50,35
    elif int(self.frame) == 21: px,py = -40,28
    elif int(self.frame) == 22: px,py = -20,10
    elif 22<int(self.frame)<25: px,py = -10,0
    elif 25<=int(self.frame)<31: px,py = -50,110
    elif int(self.frame) == 31: px,py = 0,50
    elif int(self.frame) == 32: px,py = 0,60 
    elif int(self.frame) == 33: px,py = 0,80
    elif int(self.frame) == 34: px,py = 0,90
    elif int(self.frame) == 35: px,py = 0,90
    elif int(self.frame) == 36: px,py = 0,90
    elif int(self.frame) == 37: px,py = 0,90
    elif int(self.frame) == 38: px,py = 0,85
    elif int(self.frame) == 39: px,py = 0,85
    elif int(self.frame) == 40: px,py = 0,60
    elif int(self.frame) == 41: px,py = 0,60
    if self.dir == 1: #RIGHT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'h', self.x+(-1*px), self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
         
    else: #LEFT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'n', self.x+px, self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
    
def punch_update(self):
    self.frame  = (self.frame + PUNCH_FRAMES_PER_ACTION * PUNCH_ACTION_PER_TIME * game_framework.frame_time) % 16

def punch_draw_left(self):
    global px,py
    if int(self.frame) <0:
        px,py = 0,0
    elif int(self.frame) == 1:
        px ,py = -20,55
    elif int(self.frame) == 2:
        px,py = -45,0
    elif int(self.frame) == 3:
        px,py = 50,-5
    elif int(self.frame) == 4:
        px,py = 55,-10
    elif int(self.frame) == 5:
        px,py = 60,30     
    elif int(self.frame) == 6:
        px,py = 60,-20
    elif int(self.frame) == 7:
        px,py = 60,35
    elif int(self.frame) == 8:
        px,py = 0,55
    elif int(self.frame) == 9 or int(self.frame) == 10:
        px,py = -190,50
    elif int(self.frame) == 11:
        px,py = -100,40
    elif int(self.frame) == 12:
        px,py = -60,25
    elif int(self.frame) == 13:
        px,py = -30,5
    elif int(self.frame) == 14:
        px,py = -10,-5
    elif int(self.frame) == 15:
        px,py = -5,-10
        self.jumpcount = 0
        jump(self)
    else:
        pass
    Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'n', self.x+px, self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0
def punch_draw_right(self):
    global px,py
    if int(self.frame) <0:
        px,py = 0,0
    elif int(self.frame) == 1:
        px ,py = -20,55
    elif int(self.frame) == 2:
        px,py = -45,0
    elif int(self.frame) == 3:
        px,py = 50,-5
    elif int(self.frame) == 4:
        px,py = 55,-10
    elif int(self.frame) == 5:
        px,py = 60,30     
    elif int(self.frame) == 6:
        px,py = 60,-20
    elif int(self.frame) == 7:
        px,py = 60,35
    elif int(self.frame) == 8:
        px,py = 0,55
    elif int(self.frame) == 9 or int(self.frame) == 10:
        px,py = -190,50
    elif int(self.frame) == 11:
        px,py = -100,40
    elif int(self.frame) == 12:
        px,py = -60,25
    elif int(self.frame) == 13:
        px,py = -30,5
    elif int(self.frame) == 14:
        px,py = -10,-5
    elif int(self.frame) == 15:
        px,py = -5,-10
        self.jumpcount = 0
        jump(self)
    else:
        pass
    Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0   
def jump_F_update(self):
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME  * game_framework.frame_time) % 9
    self.timer += 1
def jump_F_draw(self):
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5, Boss_Goopy.jump_F[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5, Boss_Goopy.jump_F[int(self.frame)].h//1.5)     
def jump_D_update(self):
    self.frame  = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_D_draw(self):
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
def jump_U_update(self):
    self.frame  = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_U_draw(self):
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)   
def jump(self):
    if self.y < 100:
        self.y = 100
        self.state = state['JUMP_F']
        self.jumpheight = 4
        self.jumpcount+= 1
    
    if self.jumpheight > 0:
        self.state = state['JUMP_U']
        
        F = (0.5 * self.mass * (self.jumpheight ** 2)) 
    else:
        self.state = state['JUMP_D']
        
        F = -(0.5 * self.mass * (self.jumpheight ** 2))
    
    self.y += round(F) 
    self.jumpheight -= 0.05
    if self.x < 0:
        self.dir = 1
    elif self.x > 1280:
        self.dir = -1
        
    if self.dir ==1:
        self.x += 3
    else:
        self.x -= 3
    
   