import game_framework
from pico2d import *

image = None
image_character = None
logo_time = 0.0
count = 1
def enter():
    global image, image_character
    image = load_image('title/title screen/Background/title_screen_background.png')

def exit():
    global image
    del image
    pass

def update():
    global logo_time, count, image_character
    # count = (count+1) % 34
    if count == 34:
        count = 1
    count += 1
    delay(0.01)
    image_character = load_image('title/title screen/Cuphead and Mugman/cuphead_title (%d).png' % count)

def draw():
    clear_canvas()
    image.clip_draw(0,0,1280,720,640,360)
    image_character.clip_draw(0, 0, 1280, 720, 640,250,image_character.w//1.2,image_character.h//1.2)
    update_canvas()

def handle_events():
    events = get_events()


    #현정아 11/7일 저녁에 핸들로 스페이스바 받으면 메인화면으로 넘어가게 하여라~~~