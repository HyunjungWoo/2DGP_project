from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('running_finish.png')

x, y, width, height = 0, 40, 165, 165  # 오른쪽으로 달리기
#x,y,width,height = 750,40,167,167  # 왼쪽으로 달리기
frame = 0
def draw():
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw_to_origin(frame * 165, 0, width, height, x, y, width / 2, height / 2) # 아래 위 액자크기 x,y
    update_canvas()





#왼쪽으로 뛰기



while(x<800):
    draw()
    frame = (frame + 1) % 12
    x += 5
    delay(0.25)
    get_events()







close_canvas()

