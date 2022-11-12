from pico2d import *
import game_framework
state = { 'JUMP_F':0,'Punch':1 , 'Die':2 , 'JUMP_D':3, 'JUMP_U':4}
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
PUNCH_TIME_PER_ACTION   = 10.0 #속도 조절
PUNCH_ACTION_PER_TIME   = 1.0 / PUNCH_TIME_PER_ACTION


class Boss_Goopy:
  
    def __init__(self):
        self.state = state['JUMP_F']
        self.hp = 440 
        self.image = None
        self.x,self.y = 780, 100
        self.dir = -1 #왼쪽 
        self.dirx, self.diry = -3, 0
        self.frame = 0
        self.jump_count = 0
        self.timer = 0
        self.jump_height, self.mass= 4, 1
        #self.jump_height, self.mass= 3 , 2
        #self.phase = 1      # 페이즈 1 
   
    def get_bb(self):
        return self.x - self.image.w/2 +50, self.y -self.image.h/2+50, self.x + self.image.w/2 -50,\
            self.y+ self.image.h/2 -50

   
    def update(self):
        
        if self.jump_count < 5:
            jump(self)
        else:
            self.state = state['JUMP_F']
            if self.timer == 28:
                self.state = state['Punch']
            #타이머 추가해서 멈추게 해준 후 펀치 !                        

        #상태 업데이트 조건문 
        if self.state == state['JUMP_F']:
            jump_F_update(self)
        elif self.state == state['Punch']:
            punch_update(self)
        elif self.state == state['JUMP_D']:
            jump_D_update(self)
        elif self.state == state['JUMP_U']:
            jump_U_update(self)                     
       
            
    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.dir == 1: #오른쪽 
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'h', self.x, self.y,self.image.w/1.5, self.image.h/1.5)
        else:
            self.image.clip_composite_draw(0, 0, self.image.w, self.image.h, 0, 'n', self.x, self.y,self.image.w/1.5, self.image.h/1.5)

def phase2():
    pass
def phase3():
    pass

def punch_update(self):
    self.frame  = (self.frame + PUNCH_FRAMES_PER_ACTION * PUNCH_ACTION_PER_TIME * game_framework.frame_time) % 16
    self.image = load_image('monster/Goopy/Phase 1/Punch/slime_punch(%d).png' % self.frame)
    
def jump_F_update(self):
    
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME  * game_framework.frame_time) % 9
    self.image = load_image('monster/Goopy/Phase 1/Jump/slime_jump_%d.png' % self.frame)
    self.timer += 1

def jump_D_update(self):
    self.frame  = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
    self.image = load_image('monster/Goopy/Phase 1/Air Down/air_down(%d).png' % self.frame)

def jump_U_update(self):
    self.frame  = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
    self.image = load_image('monster/Goopy/Phase 1/Air UP/air_up(%d).png' % self.frame)

    
def jump(self):
     
    if self.y < 100:
        self.y = 100
        self.state = state['JUMP_F']
        self.jump_height = 4
        self.jump_count+= 1
   
    # self.frame = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 8
    # self.image = load_image('resource/Jump/Cuphead/jump(%d).png' % self.frame)
    
    if self.jump_height > 0:
        self.state = state['JUMP_U']
        F = (0.5 * self.mass * (self.jump_height ** 2)) 
    else:
        self.state = state['JUMP_D']
        F = -(0.5 * self.mass * (self.jump_height ** 2))
    
    self.y += round(F) 
    self.jump_height -= 0.05
    if self.x < 0:
        self.dir = 1
    elif self.x > 1280:
        self.dir = -1
        
    if self.dir ==1:
        self.x += 3
    else:
        self.x -= 3
    
   