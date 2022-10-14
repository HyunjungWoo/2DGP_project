from pico2d import *
import character
from character import state, direction

# 캐릭터 속성 변경은 여기서

quitMassage = False


def check_bottom(player):  # 바닥체크
    pass


def events(CupHead):
    global state
    global direction
    global quitMassage

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료
            quitMassage = True
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 오른쪽 키 눌림
                CupHead.dirx += 1
                CupHead.direction = direction['RIGHT']
                if CupHead.state != state['JUMPING']:
                    CupHead.state = state['RUNNING']  # 상태 변경
                    CupHead.run_Frame = 0  # 프레임 초기화

            elif event.key == SDLK_LEFT:  # 왼쪽 키 눌림
                CupHead.direction = direction['LEFT']
                CupHead.dirx -= 1
                if CupHead.state != state['JUMPING']:
                    CupHead.state = state['RUNNING']  # 상태 변경
                    CupHead.run_Frame = 0  # 프레임 초기화

            elif event.key == SDLK_UP:
                
                if ( CupHead.state != state['JUMPING']):
                     CupHead.state = state['JUMPING'] 
                     CupHead.jumpSpeed  = 8
                
               
               

                pass

            elif event.key == SDLK_s:
                pass

            elif event.key == SDLK_ESCAPE:  # ESC키
                pass
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                CupHead.dirx -= 1
                CupHead.direction = direction['RIGHT']
                if CupHead.state != state['JUMPING']:
                    CupHead.state = state['STAY']
                    CupHead.stay_frame = 0
            elif event.key == SDLK_LEFT:
                CupHead.dirx += 1
                CupHead.direction = direction['LEFT']
                if CupHead.state != state['JUMPING']:
                    CupHead.state = state['STAY']
                    CupHead.stay_frame = 0
            elif event.key == SDLK_UP:
                CupHead.state = state['JUMPING']

            elif event.key == SDLK_s:
                pass
    pass
