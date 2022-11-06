from pico2d import *
import game_framework
from bullet import Bullet
import game_world
# player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# player Event
RD, LD, RU, LU ,ZD, ZU,XD= range(7) #위와 의미는 동일

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,
    (SDL_KEYDOWN,SDLK_z)      : ZD,
    (SDL_KEYUP,SDLK_z)        : ZU,
    (SDL_KEYDOWN,SDLK_x)      : XD
}
event_name = ['RD','LD','RU','LU','TIMER','SPACE']

class IDLE:
    def enter(self,event):
        print('ENTER IDLE')
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION =5

    def exit(CupHead,event):
        print('EXIT IDLE')
        if event == XD:
            CupHead.shoot()

    def do(CupHead):
        CupHead.frame = (CupHead.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    def draw(CupHead):
        CupHead.image = load_image('resource/idle/idle(%d).png' % int(CupHead.frame+1.0))
        if CupHead.face_dir > 0:
            CupHead.image.clip_composite_draw(0, 0, CupHead.image.w, CupHead.image.h, 0, 'n', CupHead.x, CupHead.y,CupHead.image.w//1.2, CupHead.image.h//1.2)
        else:
            CupHead.image.clip_composite_draw(0, 0, CupHead.image.w, CupHead.image.h, 0, 'h', CupHead.x, CupHead.y,CupHead.image.w//1.2, CupHead.image.h//1.2)


class RUN:
    def enter(CupHead, event):
        print('ENTER RUN')
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 16
        if event == RD:
            CupHead.velocity += RUN_SPEED_PPS
        elif event == LD:
            CupHead.velocity -= RUN_SPEED_PPS
        elif event == RU:
            CupHead.velocity -= RUN_SPEED_PPS
        elif event == LU:
            CupHead.velocity += RUN_SPEED_PPS
        CupHead.dir = clamp(-1, CupHead.velocity, 1)

    def exit(CupHead, event):
        print('EXIT RUN')
        CupHead.frame = 1
        CupHead.velocity = 0
        CupHead.face_dir = CupHead.dir
        if event == XD:
            CupHead.shoot()
    def do(CupHead):
        CupHead.frame = (CupHead.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        CupHead.x += CupHead.velocity * game_framework.frame_time
    def draw(CupHead):
        CupHead.image = load_image('resource/Run/Normal/run(%d).png' % int(CupHead.frame+1.0))
        if CupHead.dir == 1:
            CupHead.image.clip_composite_draw(0, 0, CupHead.image.w, CupHead.image.h, 0, 'n', CupHead.x, CupHead.y,CupHead.image.w//1.2, CupHead.image.h//1.2)
        elif CupHead.dir == -1:
             CupHead.image.clip_composite_draw(0, 0, CupHead.image.w, CupHead.image.h, 0, 'h', CupHead.x, CupHead.y,CupHead.image.w//1.2, CupHead.image.h//1.2)


next_state={
    IDLE : { RU: RUN, LU: RUN, RD: RUN, LD: RUN ,XD:IDLE} ,#동시에 누를 때도 RUN
    RUN  : { RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, XD:RUN }
}#상태 벤 다이어그램

class CupHead:

    def __init__(self):
        self.x,self.y = 1200//2,200
        self.image =load_image('resource/idle/idle(1).png')
        self.frame = 1
        self.velocity = 1
        self.dir,self.face_dir = 0,1
        self.stay_frame = 1
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__} Event {event_name[event]}')

            self.cur_state.enter(self, event)

        if self.q:  # 만약에 list q 에 뭔가 들어있으면
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def shoot(self):
        print('SHOOT')
        if self.dir !=0:
            bullet = Bullet(self.x, self.y, self.dir * 3)
            game_world.add_object(bullet, 1)
