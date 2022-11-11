from pico2d import *
from player import Player
from boss import Boss_Goopy

import game_framework
import game_world

player = None
boss = None
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
    #game_world.add_object(player, 1)
    game_world.add_object(boss,1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


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




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
