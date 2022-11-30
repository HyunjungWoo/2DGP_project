from pico2d import *
import game_framework
class HpUi:
    hp1_image = None
    hp2_image = None
    hp3_image = None
    hp_dead_img = None
    def __init__(ui,player):
        if HpUi.hp1_image == None:
            HpUi.hp1_image = load_image('UI/hp/hp_1.png')
        if HpUi.hp2_image == None:
            HpUi.hp2_image = load_image('UI/hp/hp_2.png')
        if HpUi.hp3_image == None:
            HpUi.hp3_image = load_image('UI/hp/hp_3.png')
        if HpUi.hp_dead_img == None:
            HpUi.hp_dead_img = load_image('UI/hp/hp_dead.png')    
        ui.hp = 0
        ui.frame = 0


    def update(ui,player):
         ui.hp = player.hp 
         if ui.hp == 1:
            ui.frame += game_framework.frame_time
         if ui.frame >2:
            ui.frame = 2
        
    def draw(ui,player):
        if ui.hp == 3: 
            ui.hp3_image.draw(50,30)
        elif ui.hp == 2:
            ui.hp2_image.draw(50,30)
        elif ui.hp == 1:
            ui.hp1_image.clip_draw(int(ui.frame) * 80, 0,80,33,50,30)
        elif ui.hp < 1:
            ui.hp_dead_img.draw(50,30)


