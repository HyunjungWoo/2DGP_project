from pico2d import *
import game_framework
import play_state


KNOCKOUT_FRAMES_PER_ACTION = 28 # 프레임 장수(사진 갯수)
KNOCKOUT_TIME_PER_ACTION   = 1 #속도 조절
KNOCKOUT_ACTION_PER_TIME   = 1.0 / KNOCKOUT_TIME_PER_ACTION
KnockOut = []
bgm = None
def enter():
        global KnockOutFrame,bgm
        for i in range(27):
            a = load_image('monster/Goopy/A KNOCKOUT/FightText_KO_(%d).png' % i)
            KnockOut.append(a)
        KnockOutFrame = 0 
        if bgm == None:
            bgm = load_music('UI/Sound/Knockout_bell.wav')
        bgm.set_volume(30)
        bgm.play()
def exit():
    global KnockOut,bgm
    del KnockOut,bgm

def update():
    global KnockOutFrame
    KnockOutFrame = (KnockOutFrame + KNOCKOUT_TIME_PER_ACTION+KNOCKOUT_ACTION_PER_TIME * game_framework.frame_time)%27

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
    KnockOut[int(KnockOutFrame)].draw(640,400,1280,600)
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