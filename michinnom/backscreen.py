from pico2d import *
import game_framework

SCREEN_FRAMES_PER_ACTION = 127 # 프레임 장수(사진 갯수)
SCREEN_TIME_PER_ACTION   = 0.5 #속도 조절
SCREEN_ACTION_PER_TIME   = 1.0 / SCREEN_TIME_PER_ACTION

##Tutorial 
class BackScreen: 
    images  = []
    def __init__(screen):
        for i in range(127):
            a = load_image('UI/back/screen_fx(%d).png'%i)
            BackScreen.images.append(a)
        screen.frame = 0 
    def update(screen):
        print(screen.frame)
        screen.frame = (screen.frame + SCREEN_FRAMES_PER_ACTION + SCREEN_ACTION_PER_TIME * game_framework.frame_time ) % 127

    def draw(screen):
        screen.images[int(screen.frame)].draw(600,380)

        
