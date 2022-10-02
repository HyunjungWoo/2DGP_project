from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('monster.png')



frame = 0
##몬스터 점프
for x in range(0,30):
    clear_canvas()
    character.clip_draw((frame*336)+10,1520,330,177,300,100)
        #왼쪽 아래 너비 높이
    update_canvas()
    frame = (frame + 1) % 8
    x +=5
    delay(0.25)
    get_events()

for x in range(0,30):
    clear_canvas()
    character.clip_draw((frame*268)+10,1176,262,132,300,100)
        #왼쪽 아래 너비 높이
    update_canvas()
    frame = (frame + 1) % 8
    x +=5
    delay(0.25)
    get_events()




close_canvas()
