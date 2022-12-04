import game_framework
from pico2d import *
import play_state
import ready_state
image = None
image_character = None
font = None
bgm = None
count = 1
def enter():
    global image, image_character,font,font_back,bgm
    image = load_image('resource/title/title screen/Background/title_screen_background.png')
    bgm = load_music("UI/Sound/Cuphead OST - Don't Deal With the Devil [Music].mp3")
    bgm.set_volume(30)
    bgm.repeat_play()
    font_back = load_font('FANTONY.TTF',51)
    font  = load_font('FANTONY.TTF',50 )
    
def exit():
    global image
    del image

def update():
    global  count, image_character
    
    if count == 34:
        count = 1
    count += 1
    delay(0.03)
    image_character = load_image('resource/title/title screen/Cuphead and Mugman/cuphead_title (%d).png' % count)
    
def draw():
    clear_canvas()
    image.clip_draw(0,0,1280,720,640,360)
    image_character.clip_draw(0, 0, 1280, 720, 640,250,image_character.w//1,image_character.h//1)
    font_back.draw(398,80,f'(Press SPACE BAR',(0,0,0))
    font_back.draw(395,80,f'(Press SPACE BAR',(0,0,0))   
    font.draw(400,80,f'(Press SPACE BAR)',(255,255,0))
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE or event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and  event.key == SDLK_SPACE:
            game_framework.change_state(ready_state)

def pause():
    pass

def resume():
    pass