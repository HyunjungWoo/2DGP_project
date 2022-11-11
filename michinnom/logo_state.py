import game_framework
from pico2d import *
import play_state
import ready_state
image = None
image_character = None

count = 1
def enter():
    global image, image_character
    image = load_image('resource/title/title screen/Background/title_screen_background.png')

def exit():
    global image
    del image

def update():
    global  count, image_character
    # count = (count+1) % 34
    if count == 34:
        count = 1
    count += 1
    delay(0.03)
    image_character = load_image('resource/title/title screen/Cuphead and Mugman/cuphead_title (%d).png' % count)

def draw():
    clear_canvas()
    image.clip_draw(0,0,1280,720,640,360)
    image_character.clip_draw(0, 0, 1280, 720, 640,250,image_character.w//1,image_character.h//1)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE or event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and  event.key == SDLK_SPACE:
            game_framework.change_state(ready_state)

