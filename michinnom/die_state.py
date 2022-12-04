from pico2d import *
import game_framework
import play_state

image = None
def enter():
        global image 
        if play_state.boss.phase == 1:
            image = load_image('monster/Goopy/Goopy_phase1.jpg')
        elif play_state.boss.phase ==2:
            image = load_image('monster/Goopy/Goopy_phase2.jpg')
        elif play_state.boss.phase ==3:
            image = load_image('monster/Goopy/Goopy_phase3.jpg')

def exit():
    global image
    del image

def update():
   pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(600,350)
    update_canvas()



def pause():
    pass

def resume():
    pass

def test_self():
    import die_state
    open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(die_state)
    close_canvas()

if __name__ == '__main__':
    test_self()