from pico2d import *

class CupHead_Character:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.sin = 16
        self.image2 = load_image('run_right.png')
        self.image1 = load_image('stay.png')

    def update(self):
        self.frame = (self.frame + 1) % self.sin  # 달리기
        # self.frame = (self.frame + 1 ) % scene #서있기 scene =5
        self.x += 5

    def draw(self):
        #self.image1.clip_draw(self.frame * 169, 330, 169, 225, self.x, self.y)  ## 330 간격으로 bottom 잡기 stay 이미지
        self.image2.clip_draw(self.frame * 190, 0, 190, 239, self.x, self.y)  ## 달리기 오른쪽으로 #달리기 이미지
class BackGround:
    def __init__(self):
        self.background_image = load_image('background.png')

    def draw(self):
        self.background_image.draw(600,450,1200,900)

class Potato_Monster:
    def __init__(self):
        self.frame = 0
        self.sin = 5
        self.image = load_image('potato.png')
        self.ddong = load_image('ddong.png')
        self.attack = load_image('potato_attack.png')
        self.print = 0
        self.x,self.y = 750,300
    def update(self):
        self.frame = (self.frame + 1) % self.sin
    def draw(self):
        #self.appear_motion()

        self.attack_draw()
        if(self.print>=12):
            self.ddong_draw()
    def appear_motion(self):
        pass
    def ddong_draw(self):

        self.x -= 100
        self.ddong.clip_draw(self.frame * 134, 1,133,138,self.x,100)
    def attack_draw(self):
        self.sin = 12
        self.attack.clip_draw(self.frame * 542, 0, 542, 590, 880, self.y)
        self.print += 1








open_canvas(1200,900)
background = BackGround()

potato_monster = Potato_Monster()
cuphead = CupHead_Character()
done = False

def runGame():
    global done

    while not done:
        #handle_events()
        clear_canvas()
        cuphead.update()
        background.draw()
        potato_monster.update()

        potato_monster.draw()

        cuphead.draw()



        update_canvas()

        delay(0.25)


runGame()
# close_canvas()
