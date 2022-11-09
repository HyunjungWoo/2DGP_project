from pico2d import *
import game_framework

state = {'IDLE': 0, 'RUNNING' : 1,'JUMPING':2,'AIM' : 3,'DASH':4}
direction = {'LEFT': -1, 'RIGHT':1 }

#Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH  = 30.0  # Km / Hour
RUN_SPEED_MPM   = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS   = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS   = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player Action Speed

TIME_PER_ACTION        = 1.0 #속도 조절
ACTION_PER_TIME        = 1.0 / TIME_PER_ACTION
IDLE_FRAMES_PER_ACTION = 5 # 프레임 장수(사진 갯수)
RUN_FRAMES_PER_ACTION  = 16
JUMP_FRAMES_PER_ACTION  = 8
AIM_FRAMES_PER_ACTION = 5
DASH_FRAMES_PER_ACTION = 8

DASH_TIME_PER_ACTION    = 1.0
DASH_ACTION_PER_TIME    = 1.0 / DASH_TIME_PER_ACTION
# player Event

class Player:
    def __init__(player):
        player.x, player.y = 100, 50
        player.dirx = 0
        player.direction = direction['RIGHT']
        player.image = load_image('resource/idle/idle(0).png')
        player.frame = 0
        player.jump_height, player.mass= 2 , 2
        player.state = state['IDLE']
        player.dash_count = 0
    def update(player):
        if player.state == state['IDLE']:
            Idle_update(player)
        elif player.state == state['RUNNING']:
            Run_update(player)
        elif player.state == state['JUMPING']:
            Jump_update(player)
        elif player.state == state['AIM']: 
            Aim_update(player)
        elif player.state == state['DASH']:
            Dash_update(player)
        player.x += player.dirx * 1

    def draw(player):
        if player.state == state['IDLE']:
            Idle_draw(player)
        elif player.state == state['RUNNING']:
            Run_draw(player)
        elif player.state == state['JUMPING']:
            Jump_draw(player)
        elif player.state == state['AIM']:
            Aim_draw(player)
        elif player.state == state['DASH']:
            Dash_draw(player)


    def handle_event(player, event):
        global state
        global direction
            # 키보드가 눌렸을 때
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 오른쪽 키 눌림
                player.dirx += 1
                
                if player.state != state['JUMPING']:
                    player.state = state['RUNNING']  # 상태 변경
                    player.frame = 0  # 프레임 초기화
                if player.direction == direction['LEFT'] and player.state == state['RUNNING']:
                    player.state = state['IDLE']
                    player.direction == direction['RIGHT']
                    player.direction = direction['LEFT']
                player.direction = direction['RIGHT']
            
            elif event.key == SDLK_LEFT:  # 왼쪽 키 눌림
                if player.state != state['JUMPING']:
                    player.state = state['RUNNING']  # 상태 변경
                    player.frame = 0 # 프레임 초기화
                if player.direction == direction['RIGHT'] and player.state == state['RUNNING']:
                    player.state = state['IDLE']
                player.dirx -= 1
                
                player.direction = direction['LEFT']
           
            elif event.key == SDLK_z:   
                if(player.state != state['JUMPING']):
                    player.state = state['JUMPING'] 
                        
            elif event.key == SDLK_x:
                if player.dirx !=0:
                    pass
                else:
                    player.state = state['AIM']
                    player.frame = 0
            elif event.key == SDLK_LSHIFT:
                if player.state != state['JUMPING'] and player.state != state['AIM']:
                    player.state = state['DASH']
                    player.dash_count = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dirx -= 1
                if player.state != state['JUMPING']:
                    player.state = state['IDLE']
                    player.frame = 0
                if player.direction == direction['RIGHT'] and player.state == state['IDLE']:
                    player.direction = direction['RIGHT']

            elif event.key == SDLK_LEFT:
                player.dirx += 1
                if player.direction == direction['RIGHT'] and player.state == state['IDLE']:
                    player.direction = direction['RIGHT']
                
                if player.state != state['JUMPING']:
                    player.state = state['IDLE']
                    player.frame = 0
                
            elif event.key == SDLK_z:
               
                player.frame = 0
                player.jump_height=2
                pass

            elif event.key == SDLK_v:
                if (player.state == state['Paring']):
                    player.state = state['IDLE']
                    player.frame = 0
            # elif event.key == SDLK_LSHIFT:
            #     player.state = state['IDLE']
            #     player.frame = 0
def Idle_update(player): 
    if player.dirx !=0:
        player.state = state['RUNNING']
    player.frame  = (player.frame + IDLE_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
    player.image  = load_image('resource/idle/idle(%d).png' % player.frame)

def Idle_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
            #CupHead.image.clip_composite_draw(0, 0, CupHead.image.w, CupHead.image.h, 0, 'n', CupHead.x, CupHead.y,CupHead.image.w//1.2, CupHead.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)

def Run_update(player):
        player.frame = (player.frame + RUN_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        player.image = load_image('resource/Run/Normal/run(%d).png' % player.frame)
        player.x  += player.dirx * game_framework.frame_time *RUN_SPEED_PPS

def Run_draw(player):
        
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
           
def Jump_update(player):  

    player.frame = (player.frame + JUMP_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    player.image = load_image('resource/Jump/Cuphead/jump(%d).png' % player.frame)
        
    if player.jump_height > 0:
        F = (0.5 * player.mass * (player.jump_height ** 2))
    else:
        F = -(0.5 * player.mass * (player.jump_height ** 2))
    
    player.y += round(F) 
    player.jump_height -= 0.06
    
    
    if player.y < 50:
        player.y = 50
        player.state = state['IDLE']
        player.jump_height =3
    
def Jump_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
           
def Aim_update(player):
    player.frame = (player.frame + AIM_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
    player.image = load_image('resource/aim/Straight/aim_straight(%d).png' % player.frame)

def Aim_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    
def Dash_update(player):
    # global TIME_PER_ACTION
    # TIME_PER_ACTION = 0.5
    player.frame = (player.frame + DASH_FRAMES_PER_ACTION * DASH_ACTION_PER_TIME * game_framework.frame_time) % 8
    player.image = load_image('resource/Dash/Ground/dash(%d).png' % player.frame)
    if player.direction == direction['RIGHT']:
        player.x += 3
    else:  
        player.x -= 3
    player.dash_count += 1
    if player.dash_count > 60:
        player.frame = 0
        player.state = state['IDLE']
    
    

def Dash_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
  


        
