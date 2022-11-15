from pico2d import * 
import game_framework
STREAM_FRAMES_PER_ACTION = 12 # 프레임 장수(사진 갯수)
STREAM_TIME_PER_ACTION   = 3.0 #속도 조절
STREAM_ACTION_PER_TIME   = 1.0 / STREAM_TIME_PER_ACTION

class Back_ground:
    def __init__(self):
        self.sort = 'floor'
        self.frame = 0
        self.image_back = load_image('monster/Goopy/Background/slime_bg.png')
        self.image_far_forest = load_image('monster/Goopy/Background/slime_bg_bg_far_forest.png')
        self.image_forest_bg = load_image('monster/Goopy/Background/slime_bg_bg_evergreens.png')#뒷나무
        self.image_stream = load_image('monster/Goopy/Background/slime_bg_strem(0).png') #강물
        self.image_forest= load_image('monster/Goopy/Background/slime_bg_bg_forest.png')
        
        #천장잔디들 이미지
        self.image_grass_1 = load_image('monster/Goopy/Background/slime_bg_fg_left_branch.png') #나뭇가지 왼쪽
        self.image_grass_2 = load_image('monster/Goopy/Background/slime_bg_fg_right_branches.png') #나뭇가지 오른쪽
        self.image_grass_3 = load_image('monster/Goopy/Background/slime_bg_fg_leaves_1.png') #천장 풀 1
        self.image_grass_4 =load_image('monster/Goopy/Background/slime_bg_mg_slime_2.png') #천장 덩쿨 1 
        self.image_grass_5 = load_image('monster/Goopy/Background/slime_bg_mg_slime_1.png') #천장 덩쿨 2
        
        #바닥 버섯 이미지 
        self.image_mushroom_1 = load_image('monster/Goopy/Background/slime_bg_fg_mushrooms_left.png')
        self.image_mushroom_2 = load_image('monster/Goopy/Background/slime_bg_fg_mushrooms_right.png')

    def update(self):
        self.frame  = (self.frame + STREAM_FRAMES_PER_ACTION * STREAM_ACTION_PER_TIME * game_framework.frame_time) % 12
        self.image_stream = load_image('monster/Goopy/Background/slime_bg_strem(%d).png' % self.frame)    
    
    def draw(self):
        self.image_far_forest.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2+100)
        self.image_forest_bg.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2+150)
        self.image_forest.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2+200)
        self.image_back.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2)
        self.image_stream.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2+98,720//2+12)#강물
        grass_draw(self)
        mushroom_draw(self)
        draw_rectangle(*self.get_bb())
   
    def get_bb(self):
        return 0,0,1280-1,50
    
    def handle_collision(player,ohter,group):
        pass

def grass_draw(self):
    self.image_grass_1.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',100,700)#나뭇가지 왼쪽
    self.image_grass_4.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1000,680)#덩쿨1
    self.image_grass_5.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1080,700)#덩쿨2
    self.image_grass_3.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',800,700) #천장 풀
    self.image_grass_2.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1200,700) #나뭇가지 오른쪽

def mushroom_draw(self):
    self.image_mushroom_1.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',0,50)
    self.image_mushroom_2.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1200,100)
