from pico2d import *

class Cuphead:
    def __init__(self):
        self.x,self.y = 600,80
        self.aim_frame = 1
        self.image = load_image('resource/aim/Straight/cuphead_aim_straight_0001.png')

    def update(self):
        if self.aim_frame == 6:
            self.aim_frame = 1
        self.image = load_image('resource/aim/Straight/cuphead_aim_straight_000%d.png' % (self.aim_frame))
        self.x += 10
        self.aim_frame += 1

    def draw(self):
        self.image.clip_draw(0,0,self.image.w,self.image.h,self.x,self.y)



def handle_events():
    pass

player = None

def enter():
    global player,running
    player = Cuphead()
    running = True

def exit():
    global player
    del player

def update():
    player.update()

def draw():
    clear_canvas()
    player.draw()
    update_canvas()



