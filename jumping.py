from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('ch2_jumping.png')


y = 0
frame = 0
while(y < 300):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 70,0, 74,66,30,y) #왼쪽 아래 너비 높이
    update_canvas()
    frame = (frame + 1) % 8
    y += 5
    delay(0.05)
    get_events()





close_canvas()
