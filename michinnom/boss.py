from pico2d import *
import game_framework
import game_world
import play_state
import effect
px,py = 0,0

MORPH_FRAMES_PER_ACTION = 42 # 프레임 장수(사진 갯수)
MORPH_TIME_PER_ACTION   = 5 #속도 조절
MORPH_ACTION_PER_TIME   = 1.0 / MORPH_TIME_PER_ACTION

DEATH_FRAMES_PER_ACTION = 19 # 프레임 장수(사진 갯수)
DEATH_TIME_PER_ACTION   = 7 #속도 조절
DEATH_ACTION_PER_TIME   = 1.0 /DEATH_TIME_PER_ACTION

JUMP_F_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
JUMP_F_TIME_PER_ACTION   = 10.0 #속도 조절
JUMP_F_ACTION_PER_TIME   = 1.0 / JUMP_F_TIME_PER_ACTION

Idle_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
Idle_TIME_PER_ACTION   = 3.0 #속도 조절
Idle_ACTION_PER_TIME   = 1.0 / Idle_TIME_PER_ACTION

PUNCH_FRAMES_PER_ACTION = 16 # 프레임 장수(사진 갯수)
PUNCH_TIME_PER_ACTION   = 2.5 #속도 조절
PUNCH_ACTION_PER_TIME   = 1.0 / PUNCH_TIME_PER_ACTION

INTRO_FRAMES_PER_ACTION = 16 # 프레임 장수(사진 갯수)
INTRO_TIME_PER_ACTION   = 2 #속도 조절
INTRO_ACTION_PER_TIME   = 1.0 /INTRO_TIME_PER_ACTION

MOVE_FRAMES_PER_ACTION = 7 # 프레임 장수(사진 갯수)
MOVE_TIME_PER_ACTION   = 1.0 #속도 조절
MOVE_ACTION_PER_TIME   = 1.0 /MOVE_TIME_PER_ACTION

SMASH_FRAMES_PER_ACTION = 7 # 프레임 장수(사진 갯수)
SMASH_TIME_PER_ACTION   = 1.0 #속도 조절
SMASH_ACTION_PER_TIME   = 1.0 /SMASH_TIME_PER_ACTION

DIE_FRAMES_PER_ACTION = 6 # 프레임 장수(사진 갯수)
DIE_TIME_PER_ACTION   = 1 #속도 조절
DIE_ACTION_PER_TIME   = 1.0 / DIE_TIME_PER_ACTION

state = { 'Idle':1, 'Punch':2 ,'JUMP_D':3, 'JUMP_U':4,'Morph':5, 'Death':6, 'Tomb_Intro':7 ,'Tomb_Move':8, 'Tomb_Die':9,'Tomb_Smash': 10}
class Boss_Goopy:
    jump_F =[]
    Punch = []
    jump_D = []
    jump_U = []
    Morph = []
    Death = []
    Tomb_Intro = []
    Tomb_Move = []
    Tomb_Die = []
    Tomb_Smash = []
    def load_images(self):
        for i in range(9): #Idle 제자리점프  이미지 리소스
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
        for i in range(20): #death 2페이즈 사망 이미지 리소스 
            a = load_image('monster/Goopy/Phase 2/Death/lg_slime_death(%d).png' % i)
            Boss_Goopy.Death.append(a)
        for i in range(15): #비석 Intro 이미지
            a = load_image('monster/Goopy/Phase 3/Intro/slime_tomb_fall(%d).png' % i)
            Boss_Goopy.Tomb_Intro.append(a)
        for i in range(4): #비석 move 이미지  
            a = load_image('monster/Goopy/Phase 3/Move/Right/slime_tomb_move(%d).png' % i)
            Boss_Goopy.Tomb_Move.append(a)
        for i in range(15): #비석 Smash 이미지 
            a = load_image('monster/Goopy/Phase 3/Smash/slime_tomb_smash(%d).png' % i)
            Boss_Goopy.Tomb_Smash.append(a)
        for i in range(6):#비석 Die이미지 
            a = load_image('monster/Goopy/Phase 3/Death/slime_tomb_die(%d).png' % i)
            Boss_Goopy.Tomb_Die.append(a)
        
    def __init__(self):
        self.load_images()
        self.hp = 1400 #phase 1 = 336 , phase 2= 560 phase 3= 504 full.hp = 1400 
    #'Idle':1, 'Punch':2 ,'JUMP_D':3, 'JUMP_U':4,'Morph':5, 'Death':6, 'Tomb_Intro':7 ,'Tomb_Move':8 'Tomb_Die':9,'Tomb_Smash': 10}
        self.state = state['Idle']
        self.sort = 'monster'
        self.frame = 0
        self.x,self.y = 600,100  # 기본값 y = 100 
        self.dir,self.diry = 1,0 #오른쪽
        self.jumpheight,self.mass = 4,3 #무게
        self.jumpcount = 3 # 초기값 0 설정 
        self.phase = 1# phase 1 
        self.change_morph = False  #False
        self.change_death  = False #False
        self.smash_count ,self.smash_time = 2, 0.0
        self.bosshit,self.count,self.opacify = False,0.0, 1
        
        ##이펙트 처리 ##
        self.bosseffect = effect.BossEffect(self)
       

    def update(self):
        #print(self.hp)
        if self.state == state['Idle']:
            jump_F_update(self)
        elif self.state == state['Punch']:
            punch_update(self)
        elif self.state == state['JUMP_D']:
            jump_D_update(self)
        elif self.state == state['JUMP_U']:
            jump_U_update(self)  
        elif self.state == state['Morph']:
            self.hp = 560
            morph_update(self)       
        elif self.state == state['Death']:
            death_update(self)  
        elif self.state == state['Tomb_Intro']:
            self.hp = 504 
            Intro_update(self) 
        elif self.state == state['Tomb_Die']:
            die_update(self)
        elif self.state == state['Tomb_Move']:
            move_update(self)
            self.x += self.dir*10
            if self.x < 50 :
                self.smash_count -= 1
                self.dir = 1
            elif self.x >1100:
                self.smash_count -= 1
                self.dir = -1
            if self.smash_count <0 and abs(float(self.x) - float(play_state.player.x)) < 5.0:
                self.state = state['Tomb_Smash']
                self.frame = 0
            elif self.hp < 0:
                self.state = state['Tomb_Die']
        elif self.state == state['Tomb_Smash']:
            self.smash_count = 2
            smash_update(self)
            self.smash_time += game_framework.frame_time
            if self.smash_time > 1.8:
                self.state = state['Tomb_Move']
                self.frame = 0
                self.smash_time =0.0
        if self.jumpcount <3:
            self.Jump_Goopy()
        else:
            if 504<=self.hp <1000 and self.change_morph == False:
                
                self.state = state['Morph']
            elif self.hp < 504 and self. change_death == False:
                self.state = state['Death']
            elif self.phase == 1:
                self.state = state['Punch']
            elif self.change_morph == True and self.phase == 2 and self.change_death ==False:
                self.state = state['Punch']
        if self.phase ==3:
            self.diry = 0
        self.y += self.diry*1 
        

        ##보스 피격처리 ##
        if self.bosshit == True :
            self.count += game_framework.frame_time
            if self.count > 0.5:
                self.bosshit = False
                self.count = 0 
        if self.bosshit == False:
            self.opacify = 1

        ## 보스 이펙트 업데이트 ##
        self.bosseffect.update(self)
    
    #그려주기 
    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.state == state['Idle']:
            jump_F_draw(self)
        elif self.state == state['Punch']:
            if self.phase == 1:
                punch_draw_phase1(self)
            elif self.phase == 2:
                punch_draw_phase2(self)
        elif self.state == state['JUMP_D']:
            jump_D_draw(self)
        elif self.state == state['JUMP_U']:
            jump_U_draw(self)  
        elif self.state == state['Morph']:
            morph_draw(self)
        elif self.state == state['Death']:
            death_draw(self)
        elif self.state == state['Tomb_Intro']:
            Intro_draw(self) 
        elif self.state == state['Tomb_Move']:
            move_draw(self)
        elif self.state == state['Tomb_Smash']:
            smash_draw(self)
        elif self.state == state['Tomb_Die']:
            die_draw(self)
          
            
        
        #Effect draw
        self.bosseffect.draw(self)
        
    
    #사각형 좌표값 얻기 
    def get_bb(self):
        if self.phase ==1:
            if self.state == state['Punch'] and (int(self.frame) == 9 or int(self.frame) == 10):
                if self.dir == 1: #오른쪽
                    return self.x +100 ,self.y -50,self.x +350, self.y + 200 
                else: return self.x - 350, self.y -50 , self.x -100, self.y +200 
            else:
                return self.x -50 ,self.y-50, self.x+50,self.y +50 
        elif self.phase == 2:
            if self.state == state['Punch'] and ( 13<int(self.frame)<18):
                if self.dir == 1:
                    self.y = 150
                    return self.x +100 ,self.y -40, self.x + 400, self.y + 100
                else:
                    self.y = 150
                    return self.x -100, self.y -40, self.x - 400, self.y + 100 
            return self.x -100,self.y -100,self.x + 100,self.y +100
        elif self.state == ['Death']:
            return self.x -100,self.y -50,self.x +100,self.y +50
        elif self.state == state['Tomb_Smash'] and (int(self.frame) == 10 or int(self.frame) == 11):
            return  self.x - 200,self.y -300,self.x +200, self.y-50   
        elif self.state == state['Tomb_Move'] or self.state == state['Tomb_Smash']:
            return self.x -70,self.y -30,self.x +70, self.y + 50
        elif self.state == state['Tomb_Intro'] or self.state == state['Tomb_Die']:
            return self.x -70,self.y -30,self.x +70, self.y + 50
    
    ##충돌처리
    def handle_collision(self,other,group):
        if other.sort == 'floor':
            if self.phase ==1:
                self.y = 101
            elif self.state ==state['Tomb_Smash']:
                pass
            elif self.phase ==3:
                self.y = 300
            else:    self.y = 150
            self.jumpheight = 4
            if self.jumpcount <3:
                self.state = state['Idle']
            self.jumpcount += 1 
    
        if other.sort == 'bullet':
            self.bosshit = True 
            self.opacify = 0.5 
            game_world.remove_collision_pairs(self,other,'boss:bullet')
        elif other.sort != 'bullet':
            self.bosshit = False 
        
    ## 점프 구현 
    def Jump_Goopy(self):

        if self.jumpheight > 0:
            self.frame = 0
            self.state = state['JUMP_U']
            F = (0.5* self.mass * (self.jumpheight**2)) 
        else:
            self.frame = 0
            self.state = state['JUMP_D']
            F = -(0.5 * self.mass * (self.jumpheight**2))
        self.diry = round(F)
        self.jumpheight -= 0.1
        
        if self.x < 0: 
            self.dir = 1

        elif self.x > 1280:
            self.dir = -1

        if self.dir ==1:
            if self.phase ==2:
                self.x += 7
            else:self.x += 5
        else:
            if self.phase == 2:
                self.x -= 7
            else: self.x -= 5

def punch_update(self):
    if self.phase == 1:
        self.frame  = (self.frame + PUNCH_FRAMES_PER_ACTION * PUNCH_ACTION_PER_TIME * game_framework.frame_time) % 16
    else: 
        self.frame  = (self.frame + PUNCH_FRAMES_PER_ACTION * PUNCH_ACTION_PER_TIME * game_framework.frame_time) % 19     
def punch_draw_phase1(self):
    Boss_Goopy.Punch[int(self.frame)].opacify(self.opacify)
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
        self.frame = 0
    
    if self.dir ==1: #오른쪽 
        
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    else:
        
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'n', self.x+px, self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0
def jump_D_update(self):
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_D_draw(self):
    Boss_Goopy.jump_D[int(self.frame)].opacify(self.opacify)
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
def jump_U_update(self):
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_U_draw(self):
    Boss_Goopy.jump_U[int(self.frame)].opacify(self.opacify)
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)   
def jump_F_update(self): #제자리 점프 프레임 설정 
    if self.phase == 1: 
        self.frame= (self.frame + Idle_FRAMES_PER_ACTION * Idle_ACTION_PER_TIME  * game_framework.frame_time) % 9
    elif self.phase == 2:
        self.frame= (self.frame + Idle_FRAMES_PER_ACTION * Idle_ACTION_PER_TIME  * game_framework.frame_time) % 8
def jump_F_draw(self): #제자리 점프 그리기
    Boss_Goopy.jump_F[int(self.frame)].opacify(self.opacify)
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5,Boss_Goopy.jump_F[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5, Boss_Goopy.jump_F[int(self.frame)].h//1.5)
def clear_list_and_upload_ph2(self): #리스트 안에 있는거 다 지우고  phase2 upload
    Boss_Goopy.jump_F.clear()
    Boss_Goopy.Punch.clear()
    Boss_Goopy.jump_D.clear()
    Boss_Goopy.jump_U.clear()
    for i in range(8): #Idle 제자리점프  이미지 리소스
        a = load_image('monster/Goopy/Phase 2/Jump/lg_slime_jump(%d).png' % i)
        Boss_Goopy.jump_F.append(a)
    for i in range(5): #jump_D 아래로 떨어지는 이미지 리소스 
        a = load_image('monster/Goopy/Phase 2/Air Down/lg_slime_air_down(%d).png' % i)
        Boss_Goopy.jump_D.append(a)
    for i in range(4):#jump_U 위로 올라가는 이미지 리소스
        a = load_image('monster/Goopy/Phase 2/Air UP/lg_slime_air_up(%d).png' % i)
        Boss_Goopy.jump_U.append(a)
    for i in range(19):#punch 펀치 이미지 리소스 
        a = load_image('monster/Goopy/Phase 2/Punch/lg_slime_punch(%d).png' % i)
        Boss_Goopy.Punch.append(a)
def morph_update(self):
    self.frame  = (self.frame + MORPH_FRAMES_PER_ACTION * MORPH_ACTION_PER_TIME * game_framework.frame_time) % 42
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
    elif int(self.frame) == 40:px,py = 0,60
    elif int(self.frame) == 41:
        px,py = 0,60 
        clear_list_and_upload_ph2(self)
        self.jumpcount = 0
        self.change_morph = True
        self.phase = 2
    if self.dir == 1: #RIGHT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'h', self.x+(-1*px), self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
        
    else: #LEFT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'n', self.x+px, self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
def punch_draw_phase2(self):
    Boss_Goopy.Punch[int(self.frame)].opacify(self.opacify)
    global px,py
    if int(self.frame) == 5: px ,py = -30,-2
    elif int(self.frame) == 6: px,py = 22,-5
    elif int(self.frame) == 9: px,py = 27,0
    elif int(self.frame) == 10: px,py = 27,0
    elif int(self.frame) == 11: px,py = 27,0 
    elif int(self.frame) == 12: px,py = -70,7
    elif int(self.frame) == 13: px,py = -70,7
    elif int(self.frame) == 14: px,py = -105,-7
    elif 15<=int(self.frame)<18:
        px,py = -110,0
    elif int(self.frame)==18:
        px,py = -110,0
        self.jumpcount = 0
        self.frame = 0
    if self.dir ==1: #오른쪽 
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    else:
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'n', self.x+px, self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0
def death_update(self):
    self.frame  = (self.frame + DEATH_FRAMES_PER_ACTION *DEATH_ACTION_PER_TIME * game_framework.frame_time) % 20
def death_draw(self):
    Boss_Goopy.Death[int(self.frame)].opacify(self.opacify)
    if int(self.frame)== 19 and self.change_death == False:
        phase3_monster = Fall_Tomb(self)
        game_world.add_object(phase3_monster,1)
        game_world.add_collision_pairs(play_state.boss,phase3_monster,'Boss:Tomb')
        game_world.add_collision_pairs(phase3_monster,play_state.back_ground,'Tomb:background')
        self.change_death = True

    if self.dir == 1:#오른쪽
        Boss_Goopy.Death[int(self.frame)].clip_composite_draw(0, 0, self.Death[int(self.frame)].w, Boss_Goopy.Death[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.Death[int(self.frame)].w//1.5,Boss_Goopy.Death[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.Death[int(self.frame)].clip_composite_draw(0, 0, self.Death[int(self.frame)].w, Boss_Goopy.Death[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.Death[int(self.frame)].w//1.5, Boss_Goopy.Death[int(self.frame)].h//1.5)
def Intro_update(self):
    self.frame = (self.frame +INTRO_FRAMES_PER_ACTION * INTRO_ACTION_PER_TIME*game_framework.frame_time )%16
def Intro_draw(self):
    if int(self.frame) ==15:   
        self.frame = 0     
        self.state = state['Tomb_Move']
    if self.dir == 1:#오른쪽
        Boss_Goopy.Tomb_Intro[int(self.frame)].clip_composite_draw(0, 0,Boss_Goopy.Tomb_Intro[int(self.frame)].w,Boss_Goopy.Tomb_Intro[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.Tomb_Intro[int(self.frame)].w//1.2,Boss_Goopy.Tomb_Intro[int(self.frame)].h//1.2)
    else:
        Boss_Goopy.Tomb_Intro[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Tomb_Intro[int(self.frame)].w, Boss_Goopy.Tomb_Intro[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.Tomb_Intro[int(self.frame)].w//1.2, Boss_Goopy.Tomb_Intro[int(self.frame)].h//1.2)
def move_update(self):
    self.frame = (self.frame +MOVE_FRAMES_PER_ACTION * MOVE_ACTION_PER_TIME*game_framework.frame_time ) % 4
def move_draw(self):
    Boss_Goopy.Tomb_Move[int(self.frame)].opacify(self.opacify)
    if self.dir == 1:#오른쪽
        Boss_Goopy.Tomb_Move[int(self.frame)].clip_composite_draw(0, 0,Boss_Goopy.Tomb_Move[int(self.frame)].w,Boss_Goopy.Tomb_Move[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.Tomb_Move[int(self.frame)].w//1.2,Boss_Goopy.Tomb_Move[int(self.frame)].h//1.2)
    else:
        Boss_Goopy.Tomb_Move[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Tomb_Move[int(self.frame)].w, Boss_Goopy.Tomb_Move[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.Tomb_Move[int(self.frame)].w//1.2, Boss_Goopy.Tomb_Move[int(self.frame)].h//1.2)
def smash_update(self):
    self.frame = (self.frame + SMASH_FRAMES_PER_ACTION * SMASH_ACTION_PER_TIME * game_framework.frame_time) %15
def smash_draw(self):
    Boss_Goopy.Tomb_Smash[int(self.frame)].opacify(self.opacify)
    global px,py
    if int(self.frame)   == 6 : px ,py = 0,35
    elif int(self.frame) == 7 : px,py = 0,10
    elif int(self.frame) == 8 : px,py = -50,-102
    elif int(self.frame) == 9 : px,py = 0,-140
    elif int(self.frame) ==10 : px,py = -50,-200
    elif int(self.frame) ==11 : px,py = 0,-200
    elif int(self.frame) ==12 : px,py = 0,-140
    elif int(self.frame) ==13 : px,py = 0,-50
    elif int(self.frame) ==14 : 
        self.state = state['Tomb_Move']
    else: px,py = 0,0 

    if self.dir ==1: #오른쪽 
        Boss_Goopy.Tomb_Smash[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Tomb_Smash[int(self.frame)].w,  Boss_Goopy.Tomb_Smash[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py, Boss_Goopy.Tomb_Smash[int(self.frame)].w/1.5,  Boss_Goopy.Tomb_Smash[int(self.frame)].h/1.5)
    else:
        Boss_Goopy.Tomb_Smash[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Tomb_Smash[int(self.frame)].w,  Boss_Goopy.Tomb_Smash[int(self.frame)].h, 0, 'n', self.x+px,self.y+py, Boss_Goopy.Tomb_Smash[int(self.frame)].w/1.5,  Boss_Goopy.Tomb_Smash[int(self.frame)].h/1.5)
def die_update(self):
    self.frame = (self.frame +DIE_FRAMES_PER_ACTION * DIE_ACTION_PER_TIME*game_framework.frame_time )%6
def die_draw(self):
    if self.dir == 1:#오른쪽
        
        Boss_Goopy.Tomb_Die[int(self.frame)].clip_composite_draw(0, 0,Boss_Goopy.Tomb_Die[int(self.frame)].w,Boss_Goopy.Tomb_Die[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.Tomb_Die[int(self.frame)].w//1.2,Boss_Goopy.Tomb_Die[int(self.frame)].h//1.2)
    else:
        Boss_Goopy.Tomb_Die[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Tomb_Die[int(self.frame)].w, Boss_Goopy.Tomb_Die[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.Tomb_Die[int(self.frame)].w//1.2, Boss_Goopy.Tomb_Die[int(self.frame)].h//1.2)


class Fall_Tomb:
    image = None
    def __init__(Tomb,boss):
        Tomb.sort = 'Tomb'
        if Fall_Tomb.image == None:
            Fall_Tomb.image = load_image('monster/Goopy/Phase 3/Intro/slime_tomb_fall_0001.png')
        Tomb.x = boss.x
        Tomb.y = 900
        Tomb.dirx,Tomb.diry = 1,3
        Tomb.dir = boss.dir 
        Tomb.frame = 0
        Tomb.state = None
        Tomb.floor = False
    def update(Tomb):
        if Tomb.diry != 0:
            Tomb.y -= Tomb.diry *3   
        
    def draw(Tomb):
        draw_rectangle(*Tomb.get_bb())
        Tomb.image.draw(Tomb.x, Tomb.y, Tomb.image.w//1.2, Tomb.image.h//1.2)
            
    def get_bb(Tomb): 
        return Tomb.x - 150, Tomb.y - 150 , Tomb.x + 150, Tomb.y + 150
   
    def handle_collision(Tomb,other,group):
        if other.sort =='monster':
           other.state = state['Tomb_Intro']
           other.phase = 3 
           other.frame = 0
           other.jump_count = 3
           other.y = 300
           game_world.remove_object(Tomb)
          

            
        
