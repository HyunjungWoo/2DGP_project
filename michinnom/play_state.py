from pico2d import *
from player import Player
from boss import Boss_Goopy
from background import Back_ground
player_state = {'IDLE': 0, 'RUNNING' : 1,'JUMPING':2,'AIM' : 3,'DASH':4, 'SHOOT':5, 'RUN_SHOOT':6, 'DUCK':7,'HIT':8}
import game_framework
import game_world

player = None
boss = None
back_ground = None
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
           player.handle_event(event)

# 초기화
def enter():
    global player,boss
    player = Player()
    boss = Boss_Goopy()
    back_ground = Back_ground()
    game_world.add_object(player, 1)
    game_world.add_object(boss,1)
    game_world.add_object(back_ground,0)
    game_world.add_collision_pairs(player,boss,'player:boss')
    game_world.add_collision_pairs(boss,back_ground,'boss:background')
    game_world.add_collision_pairs(player,back_ground,'player:background')
    
    

# 종료
def exit():
    game_world.clear()

def update():
    global player,boss
    for game_object in game_world.all_objects():
        game_object.update()
    
    for a,b, group in game_world.all_collision_pairs():
        if collide(a,b):
            #print('COLLISION ',group)
            a.handle_collision(b,group)
            b.handle_collision(a,group)
    # if collide(player, boss):
    #     print('COLLISION playert:boss')
    #     player.change_state(player_state['HIT'])
    #     print(player.state)
def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b ,right_b, top_b = b.get_bb()
    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True 


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
