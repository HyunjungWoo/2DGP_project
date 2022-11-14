from pico2d import * 
        
class Back_ground:
    def __init__(self):
        self.sort = 'floor'
        self.image_back = load_image('monster/Goopy/Background/slime_bg.png')
        self.image_forest_bg = load_image('monster/Goopy/Background/slime_bg_bg_evergreens.png')
        self.image_forest = load_image('monster/Goopy/Background/slime_bg_bg_forest.png')
    def update(self):
        pass
    def draw(self):
        self.image_forest_bg.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2+100)
        self.image_forest.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2+100)
        self.image_back.clip_composite_draw(0,0,self.image_back.w,self.image_back.h,0,'n',1280//2,720//2)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return 0,0,1280-1,50
    def handle_collision(player,ohter,group):
        pass