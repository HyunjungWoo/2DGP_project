from pico2d import *
import game_framework
import game_world
from bullet import Bullet
state = {'IDLE': 0, 'RUNNING' : 1,'JUMPING':2,'AIM' : 3,'DASH':4, 'SHOOT':5, 'RUN_SHOOT':6, 'DUCK':7}
direction = {'LEFT': -1, 'RIGHT':1 , 'UP':2, 'DOWN':0 }

#Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH  = 30.0  # Km / Hour
RUN_SPEED_MPM   = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS   = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS   = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player Action Speed


IDLE_FRAMES_PER_ACTION = 5 # 프레임 장수(사진 갯수)
IDLE_TIME_PER_ACTION   = 1.0 #속도 조절
IDLE_ACTION_PER_TIME   = 1.0 / IDLE_TIME_PER_ACTION

RUN_FRAMES_PER_ACTION  = 16
RUN_TIME_PER_ACTION    = 0.5 #속도 조절
RUN_ACTION_PER_TIME    = 1.0 / RUN_TIME_PER_ACTION

JUMP_FRAMES_PER_ACTION  = 8
JUMP_TIME_PER_ACTION    = 0.3#속도 조절
JUMP_ACTION_PER_TIME    = 1.0 / JUMP_TIME_PER_ACTION

AIM_FRAMES_PER_ACTION = 5
AIM_TIME_PER_ACTION   = 0.8 #속도 조절
AIM_ACTION_PER_TIME   = 1.0 / AIM_TIME_PER_ACTION

DASH_FRAMES_PER_ACTION = 8
DASH_TIME_PER_ACTION   = 1.0
DASH_ACTION_PER_TIME   = 1.0 / DASH_TIME_PER_ACTION

DUCK_FRAMES_PER_ACTION = 13
DUCK_TIME_PER_ACTION   = 0.8
DUCK_ACTION_PER_TIME   = 1.0 / DASH_TIME_PER_ACTION
# player Event

class Player:
    def __init__(player):
        player.x, player.y = 100, 100
        player.dirx = 0
        player.direction = direction['RIGHT']
        player.image = load_image('resource/idle/idle(0).png')
        player.frame = 0
        player.jump_height, player.mass= 3 , 2
        player.state = state['IDLE']
        player.dash_count, player.jump_count = 0, 0
    
    def get_bb(player):
        return player.x - player.image.w/2, player.y -player.image.h/2, player.x + player.image.w/2 , player.y+ player.image.h/2
   
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
        elif player.state == state['SHOOT']:
            Shoot_update(player)
        elif player.state == state['RUN_SHOOT']:
            Run_shoot_update(player)
        elif player.state == state['DUCK']:
            Duck_update(player)
        player.x += player.dirx * 1
      
    def draw(player):
        draw_rectangle(*player.get_bb())
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
        elif player.state == state['SHOOT']:
            Shoot_draw(player)
        elif player.state == state['RUN_SHOOT']:
            Run_Shoot_draw(player)
        elif player.state == state['DUCK']:
            Duck_draw(player)
    
    def fire_bullet(player):
        bullet =  Bullet(player)
        game_world.add_object(bullet,1)

    def handle_event(player, event):
        global state
        global direction
            # 키보드가 눌렸을 때
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 오른쪽 키 눌림
                player.direction = direction['RIGHT']
                if player.state != state['AIM'] or player.state != state['DUCK'] :
                    player.dirx += 1 # x값 증가 
                
                if player.state != state['JUMPING'] and player.state != state['DASH'] and player.state != state['AIM']:
                    player.state = state['RUNNING']  # 상태 변경
                    player.frame = 0 
                     # 프레임 초기화
                if player.direction == direction['LEFT'] and player.state == state['RUNNING']:
                    player.state = state['IDLE']
                   
            elif event.key == SDLK_LEFT:
                player.direction = direction['LEFT']  # 왼쪽 키 눌림
                if player.state != state['AIM']  or player.state != state['DUCK'] :
                   player.dirx -= 1

                if player.state != state['JUMPING'] and player.state != state['DASH'] and player.state != state['AIM']:
                    player.state = state['RUNNING']  # 상태 변경
                    player.frame = 0 # 프레임 초기화

                if player.direction == direction['RIGHT'] and player.state == state['RUNNING']: #방향키 누른상태로 전환 
                    player.state = state['IDLE']
               
            elif event.key == SDLK_c:
                if player.dirx !=0:
                    pass
                elif player.state != state['DASH'] and player.state != state['JUMPING']: 
                    player.state = state['AIM']
                    player.frame = 0

            elif event.key == SDLK_x:
                player.fire_bullet()
                if player.state != state['DASH'] and player.state != state['JUMPING']:
                    if player.state == state['IDLE']:
                        player.state = state['SHOOT']
                    elif player.state == state['AIM']:
                        player.state = state['SHOOT']
                    elif player.state == state['RUNNING']:
                        player.state = state['RUN_SHOOT']
                    
                    
            elif event.key == SDLK_UP:
                if player.state == state['AIM'] or player.state == state['SHOOT']:
                 player.direction = direction['UP']
            
            elif event.key ==  SDLK_DOWN:    
                if player.state == state['AIM'] or player.state == state['SHOOT']:
                 player.direction = direction['DOWN']
                
                elif  player.state != state['JUMPING'] and player.state !=state['AIM']:
                    player.state = state['DUCK']
                    player.dirx = 0 
                
                elif player.state == state['IDLE'] and player.direction == direction['DOWN']:
                    player.state = state['DUCK']
                    player.dirx =0 
                
            elif event.key == SDLK_z:  
                
                if(player.jump_count < 1 and player.state != state['JUMPING']):
                    player.jump_count += 1 
                    player.state = state['JUMPING'] 
                    player.frame = 0 
                    player.jump_height = 3

            elif event.key == SDLK_LSHIFT:
                # if player.state != state['JUMPING'] and player.state != state['AIM']:
                if player.state != state['AIM']:
                    player.state = state['DASH']
                    player.dash_count = 0

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if player.state == state['AIM'] or player.state == state['IDLE'] or player.state == state['DUCK']:
                    player.dirx =0 
                else:
                    player.dirx -= 1
                
                if player.state != state['JUMPING'] and player.state != state['DASH']:
                    player.state = state['IDLE']
                    player.frame = 0
                if player.direction == direction['RIGHT'] and player.state == state['IDLE']:
                    player.direction = direction['RIGHT']

            elif event.key == SDLK_LEFT:
                if player.state == state['AIM'] or player.state == state['IDLE'] or player.state == state['DUCK']:
                    player.dirx =0 
                else:
                    player.dirx += 1
                
                if player.direction == direction['RIGHT'] and player.state == state['IDLE']:
                    player.direction = direction['LEFT']
                
                if player.state != state['JUMPING'] and player.state != state['DASH'] and player.state != state['AIM']:
                    player.state = state['IDLE']
                    player.frame = 0
            elif event.key == SDLK_DOWN:
                if player.state != state['SHOOT'] and player.state== state['DUCK']:
                    player.state = state['IDLE']
            elif event.key == SDLK_z:
                pass
            elif event.key == SDLK_c:
                if player.state == state['AIM']:
                    player.state =  state['IDLE']
                    player.frame = 0 
                    player.direction = direction['RIGHT']
            elif event.key == SDLK_x:
                player.frame = 0            
                if player.state == state['RUN_SHOOT']:
                    player.state = state['RUNNING']                    
                elif player.state == state['SHOOT']:
                    player.state = state['IDLE']    
            

def Idle_update(player): 
    if player.dirx !=0:
        player.state = state['RUNNING']
    player.frame  = (player.frame + IDLE_FRAMES_PER_ACTION * IDLE_ACTION_PER_TIME * game_framework.frame_time) % 5
    player.image  = load_image('resource/idle/idle(%d).png' % player.frame)
def Idle_draw(player):
    if player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    else:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
def Run_update(player):
        player.frame = (player.frame + RUN_FRAMES_PER_ACTION * RUN_ACTION_PER_TIME * game_framework.frame_time) % 16
        player.image = load_image('resource/Run/Normal/run(%d).png' % player.frame)
        player.x  += player.dirx * game_framework.frame_time *RUN_SPEED_PPS
def Run_draw(player):
        
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)    
def Run_shoot_update(player):
        player.frame = (player.frame + RUN_FRAMES_PER_ACTION * RUN_ACTION_PER_TIME * game_framework.frame_time) % 14
        player.image = load_image('resource/Run/Shooting/Straight/run_shoot (%d).png' % player.frame)
        player.x  += player.dirx * game_framework.frame_time *RUN_SPEED_PPS
def Run_Shoot_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)    
def Jump_update(player):  
    
    if player.y < 100:
        player.y = 100
        player.state = state['IDLE']
        player.jump_height = 3
        player.jump_count = 0
    
    player.frame = (player.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 8
    player.image = load_image('resource/Jump/Cuphead/jump(%d).png' % player.frame)
    
    if player.jump_height > 0:
        F = (0.5 * player.mass * (player.jump_height ** 2)) 
    else:
        F = -(0.5 * player.mass * (player.jump_height ** 2))
    
    player.y += round(F) 
    player.jump_height -= 0.05
def Jump_draw(player):
    if player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)   
    else:  
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)     
def Aim_update(player):
    player.frame = (player.frame + AIM_FRAMES_PER_ACTION * AIM_ACTION_PER_TIME * game_framework.frame_time) % 5
    if player.direction == direction['RIGHT'] or player.direction == direction['LEFT']:
        player.image = load_image('resource/aim/Straight/aim_straight(%d).png' % player.frame)
    elif player.direction == direction['UP']:
        player.image = load_image('resource/aim/Up/aim_Up(%d).png'% player.frame)
    elif player.direction == direction['DOWN']:
        player.image = load_image('resource/aim/Down/aim_Down(%d).png'% player.frame)
def Aim_draw(player):
    if player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    else:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2) 
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
        player.state = state['JUMPING']
        
        player.jump_height = 0    
def Dash_draw(player):
    if player.direction == direction['RIGHT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    elif player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
def Shoot_update(player):
    player.frame = (player.frame + AIM_FRAMES_PER_ACTION * AIM_ACTION_PER_TIME * game_framework.frame_time) % 6
    if player.direction == direction['RIGHT'] or player.direction == direction['LEFT']:
        player.image = load_image('resource/Shoot/Straight/shoot_straight (%d).png' % player.frame)
    elif player.direction == direction['UP']:
        player.image = load_image('resource/Shoot/Up/shoot_up (%d).png'% player.frame)
    elif player.direction == direction['DOWN']:
        player.image = load_image('resource/Shoot/Down/shoot_down (%d).png'% player.frame)
def Shoot_draw(player):
    if player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y,player.image.w//1.2, player.image.h//1.2)
    else:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y,player.image.w//1.2, player.image.h//1.2) 
def Duck_update(player):
    
    player.frame = (player.frame + DUCK_FRAMES_PER_ACTION * DUCK_ACTION_PER_TIME * game_framework.frame_time) % 13
    player.image = load_image('resource/Duck/Idle/duck(%d).png' % player.frame) 
def Duck_draw(player):
    if player.direction == direction['LEFT']:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'h', player.x, player.y-30,player.image.w//1.2, player.image.h//1.2)
    else:
        player.image.clip_composite_draw(0, 0, player.image.w, player.image.h, 0, 'n', player.x, player.y-30,player.image.w//1.2, player.image.h//1.2) 

    