from pico2d import *



#character1 = load_image('')
#character.clip_draw(self,left,bottom,width,height,x,y,w,h)


'''목표조건
    1. 캐릭터가 움직이도록 한다 좌우이동, 제자리, 위(점프),아래(앉기)
    2. 몬스터가 어떻게 움직일 지 설정한다 
    3. 몬스터와 캐릭터의 상호작용
    4. 추가 조건 캐릭터 가속도 중력 적용 등등'''



## 10/1일차
## 캐릭터 구현 : 왼쪽 오른쪽 달리기 구현완료
##  앉기 (수정필요)

## 캐릭터 구현: 왼쪽 오른쪽 달리기 ,점프,가만히 , 앉기 구현





def handle_events():   #이벤트
    global running  # 뛰기 글로벌 변수
    global duck  #앉기 글로벌 변수
    global dirx,de,diry  # dirx = x값증가량 diry= y값 증가량 de = 이미지의 방향설정을 위해 만든 변수 (스크립트시트)

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:  ## 키 누를 때
            if event.key == SDLK_RIGHT:  ## 오른쪽
                de= 0
                dirx += 3
            elif event.key == SDLK_LEFT: ##왼쪽
                de = 1
                dirx -= 3
            elif event.key == SDLK_DOWN: ##아래
                if(running == True):
                    running = False
                    duck = True
            elif event.key == SDLK_ESCAPE:## esc
                running = False

        elif event.type == SDL_KEYUP:  ## 키를 뗐을 때
            if event.key == SDLK_RIGHT: ##오른쪽
                de = 0
                dirx -= 3
            elif event.key == SDLK_LEFT:##왼쪽
                de = 1
                dirx += 3
            elif event.key == SDLK_DOWN:##아래
                duck = False
                running = True





open_canvas(1800,900)

im_run = load_image('running.png') ## 달리기 이미지 로드
im_gs = load_image('ghost2.png')##유령모드 이미지 로드
im_jum = load_image('jump.png') ## 점프하는 이미지 로드
im_down = load_image('duck.png') ##앉기 이미지 로드


x = 1800//2  #맵 가로
y = 900//2  #맵 세로
frame = 0
de = 0
dirx = 0
diry = 0

#ghost = True

#running = True
#jumping = True
#duck = False
jumping = True
##유령모드
'''while(ghost):
    clear_canvas()
    im_gs.clip_draw((frame * 120), 0, 120, 218, x, y)
    update_canvas()
    frame = (frame + 1) % 7
    delay(0.25)
'''

#달리기   -- 가속도 추가 추가해야함 달리기에
'''while(running):
    clear_canvas()
    im_run.clip_draw((frame *157)+24, 265 * de ,157, 264,x,y)##달리기 자르는 거

    update_canvas()

    handle_events()
    frame = (frame + 1) % 15  # 아래 위 액자크기 x,y
    x += dirx * 5
    y += diry * 5
    delay(0.05)'''

#점프
while(jumping):
    clear_canvas()
    im_jum.clip_draw((frame * 124) ,0,127,125,x,y)
    update_canvas()

    frame = (frame +1) % 15
    delay(0.01)

'''
#앉기
#수정필요 오류 걸림 앉기 후 바로 꺼짐
while(duck):
    clear_canvas()
    im_down.clip_draw((frame *171),0,162,132,x,y)
    update_canvas()

    handle_events()
    frame = (frame + 1 ) % 13
    delay(0.25)
'''



close_canvas()















