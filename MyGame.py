from pico2d import *
import character_handle

open_canvas(1200, 900)
background_image = load_image('background.png')
Monster = character_handle.character.Potato_Monster()
player = character_handle.character.CupHead()


'''while (not character_handle.quitMassage):
    player.update()
    Monster.update()
    
    clear_canvas()cc
    
    background_image.draw(600,450,1200,900)
    Monster.draw()
    player.draw()
    update_canvas()
    delay(0.06)
    character_handle.events(player)  # 이벤트 처리

close_canvas()
'''

def runGame():


    while not character_handle.done:
        player.update()
        Monster.update()

        clear_canvas()

        background_image.draw(600, 450, 1200, 900)

        Monster.draw()
        player.draw()

        update_canvas()
        delay(0.05)
        character_handle.events(player)
        # 이벤트 처리

runGame()