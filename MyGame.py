from pico2d import *
import manage

open_canvas(1200, 900)
background_image = load_image('background.png')
Monster = manage.character.Potato_Monster()
player = manage.character.CupHead()

while (not manage.quitMassage):
    player.update()
    Monster.update()
    
    clear_canvas()
    
    background_image.draw(600,450,1200,900)
    Monster.draw()
    player.draw()
    update_canvas()
    delay(0.07)
    manage.events(player)  # 이벤트 처리

close_canvas()