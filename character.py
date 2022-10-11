from pico2d import *

class CupHead_Character:
    def __init__(self):
        self.x,self.y = 0,90
        self.stay_frame = 0
        self.run_frame = 0
        self.image2 = load_image('run_right.png')
        self.image1 = load_image('stay.png')
    def update(self):
        self.run_frame = (self.run_frame + 1 ) % 16
        self.stay_frame = (self.stay_frame + 1 ) % 5
        self.x += 5

    def stay_draw(self):
        self.image1.clip_draw(self.stay_frame * 169,330,169,225,self.x,self.y)## 330 간격으로 bottom 잡기

    def run_draw(self):
        self.image2.clip_draw(self.run_frame * 190,0,190,239,self.x,self.y)  ## 달리기 오른쪽으로




open_canvas()
cuphead = CupHead_Character()
running = True

while running:

    #handle_events()

    cuphead.update()

    clear_canvas()
    #cuphead.stay_draw()
    cuphead.run_draw()
    update_canvas()

    delay(0.25)



close_canvas()
