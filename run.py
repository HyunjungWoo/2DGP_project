from pico2d import *

def handle_events():   #이벤트
    # 밖에있는거 함수에서 써주려면 글로벌 선언 무조건 하고
    global running,state,direction,RIGHT,LEFT,STAY,jumping
    global frame_runRight,frame_runLeft,frame_stay,frame_jump #달리고 있는 상태 변수
    global dirx,diry,velocity,mass

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:

            running = False

        elif event.type == SDL_KEYDOWN: ## 키 누를 때
            if event.key == SDLK_RIGHT:  ## 오른쪽

                state = running
                direction = RIGHT
                frame_runRight = 1 # 버튼을 누르면 frame값 초기화
                dirx += 1

            elif event.key == SDLK_LEFT: ##왼쪽

                state = running
                direction = LEFT
                frame_runLeft = 1
                dirx -= 1

            elif event.key == SDLK_DOWN: ##아래
                pass

            elif event.key == SDLK_UP:
                state = jumping
                frame_jump = 1


            elif event.key == SDLK_ESCAPE: ##esc

                running = False

        elif event.type == SDL_KEYUP:  ## 키를 뗐을 때

            

            if event.key == SDLK_RIGHT: ##오른쪽
                direction = RIGHT
                dirx -= 1
                if(not state == jumping):
                    state = STAY
                    frame_stay = 1
            elif event.key == SDLK_LEFT:##왼쪽
                direction = LEFT
                dirx += 1
                if(not state == jumping):
                    state = STAY
                    frame_stay = 1
                
            elif event.key == SDLK_DOWN:##아래
                pass

            elif event.key == SDLK_UP:
                velocity = 7


sprit = 'runRight '
sprit2 = 'runLeft '
stay = 'stay '
stay_left = 'stay_'
jump = 'jump '

# 스프라이트 숫자값 따로 받으셈

frame_stay = 1
frame_runLeft = 1
frame_runRight = 1
frame_jumping = 1

# 변수들 쓸거면 초기화 전부 제대로 하고 쓰세요
# 상태 변수들 숫자 다르게 하세요 그리고 쓸 때 다른 변수랑 숫자 안 겹치는지 체크 잘하세요 겹쳐도 되긴 하는데 state 검사할 때 조심
jumping = 2
running = 1
STAY = 0
state = STAY
RIGHT = 1
LEFT = 0
direction = RIGHT
dirx =0

velocity,mass =7,1
x ,y= 800//2,400//2

width=1200
height= 900
bottom = 200
open_canvas(width,height)
# sky = load_image('sky.png')
# yard = load_image('yard.png')
F =0
while(1):
    if(state == STAY and direction == RIGHT):
        if frame_stay == 6:
            frame_stay = 1
        im_run = load_image('resource/idle/idle(%d).png'% (stay, frame_stay))
        frame_stay += 1
        delay(0.075)
    elif(state == STAY and direction == LEFT):
        if frame_stay == 6:
            frame_stay = 1
        im_run = load_image('%s(%d).png' % (stay_left, frame_stay))
        frame_stay += 1
        delay(0.075)
    elif(state == running):
        if(direction == RIGHT):
            if frame_runRight == 17:
                frame_runRight = 1
            im_run = load_image('%s(%d).png' % (sprit, frame_runRight))
            frame_runRight += 1
            delay(0.05)
        elif(direction == LEFT):
             if frame_runLeft == 10:
                frame_runLeft = 1
             im_run = load_image('%s(%d).png' % (sprit2, frame_runLeft))
             frame_runLeft += 1
             delay(0.05)
    elif(state == jumping):



        if velocity > 0:
            F = (0.5 * mass * (velocity * velocity))

        else:
            #속도가 0보다 작을 때는 아래로 내려감
            F = -(0.5 * mass * (velocity * velocity))

        #좌표 수정: 위로 올라가기 위해서는 y좌표를 줄여준다
        y  += int(F)

        velocity -= 1

        if bottom >= y:
            state = STAY
            y = 200

        delay(0.05)

    clear_canvas()
    sky.clip_draw(0,0,1200,900,600,460)
    x += dirx * 5

    im_run.clip_draw(0, 0, im_run.w, im_run.h, x,  y)
    update_canvas()

    handle_events() # 이거 그냥 getevents로 받지마라

