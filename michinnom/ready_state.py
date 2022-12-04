import game_framework
from pico2d import *
import play_state
import logo_state
import game_world
from background import Back_ground
image_ready_and_Wallop,image_character, image_boss_monster = None,None,None
bgm= None
count_logo,count_chracter,count_boss = 2,1,1
back_ground = None
def enter():
    global back_ground,bgm
    back_ground = Back_ground()
    global  image_ready_and_Wallop
    global image_character
    global image_boss_monster
    bgm = load_music('ready_state.mp3')
    bgm.set_volume(20)
    bgm.play()


def exit():
    global image_ready_and_Wallop,image_character, image_boss_monster,back_ground,bgm
    del image_ready_and_Wallop,image_character , image_boss_monster,back_ground,bgm

def update():
    back_ground.update()
    logo_update()
    chracter_update()
    boss_update()
    delay(0.06)

def chracter_update():
    global count_chracter, image_character
    if count_chracter == 29: #캐릭터 움직이는 그림
        count_chracter = 1
    else:
        image_character = load_image('resource/Intros/Regular/cuphead_intro (%d).png' % count_chracter)
    count_chracter += 1

def logo_update():
    global  count_logo, image_ready_and_Wallop
    if count_logo == 52:
        game_framework.change_state(play_state)
    else:
        image_ready_and_Wallop = load_image('resource/Ready,WALLOP!/FightText_GetReady_000%d.png'%count_logo)    
    count_logo += 1

def boss_update():
    global count_boss, image_boss_monster
    if count_boss == 28:    
        count_boss= 1
    else:
        image_boss_monster = load_image('monster/Goopy/Phase 1/Intro/slime_intro (%d).png'%count_boss)    
    count_boss += 1
    
    
def draw():
    clear_canvas()
    back_ground.draw()
    image_ready_and_Wallop.clip_draw_to_origin(0, 0, image_ready_and_Wallop.w, image_ready_and_Wallop.h,0, 30, image_ready_and_Wallop.w*2.5, image_ready_and_Wallop.h*2.5)
    image_character.clip_draw_to_origin(0, 0, image_character.w, image_character.h, 100, 50, image_character.w/1.2, image_character.h/1.2)
    image_boss_monster.clip_draw_to_origin(0, 0, image_boss_monster.w, image_boss_monster.h, 780, 50, w=None, h=None)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.change_state(logo_state)
            #ready_state 멈추기 상태 구현 필요 


def pause():
    pass

def resume():
    pass
       

