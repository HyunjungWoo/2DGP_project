from pico2d import *
import game_framework
import random
### INTRO DUST ###
INTRODUST_FRAMES_PER_ACTION = 36 # 프레임 장수(사진 갯수)
INTRODUST_TIME_PER_ACTION   = 2 #속도 조절
INTRODUST_ACTION_PER_TIME   = 1.0 / INTRODUST_TIME_PER_ACTION

### MOVE DUST ###
MOVEDUST_FRAMES_PER_ACTION = 4 # 프레임 장수(사진 갯수)
MOVEDUST_TIME_PER_ACTION   = 3 #속도 조절
MOVEDUST_ACTION_PER_TIME   = 1.0 / MOVEDUST_TIME_PER_ACTION

### DIE SPARK ###
DIESPARK_FRAMES_PER_ACTION = 7 # 프레임 장수(사진 갯수)
DIESPARK_TIME_PER_ACTION   = 30 #속도 조절
DIESPARK_ACTION_PER_TIME   = 1.0 / DIESPARK_TIME_PER_ACTION


class BossEffect:
    Tomb_Intro_img = []
    Tomb_Move_img = []
    Tomb_Smash_img = []
    Tomb_Die_img = []
    Tomb_Die_dust = None
    Slime_explode_img= []
    Slime_dust_img = []
    def __init__(effect,boss):
        #인트로 이미지 초기화
        for i in range(36):
           a = load_image('monster/Goopy/Phase 3/Dust(Intro)/slime_tomb_dust(%d).png' % i )
           BossEffect.Tomb_Intro_img.append(a)
        for i in range(4):
           a = load_image('monster/Goopy/Phase 3/Move/GroundFX/Dust/slime_tomb_groundfx(%d).png' % i )
           BossEffect.Tomb_Move_img.append(a)
        for i in range(17):
            a = load_image('monster/Goopy/Phase 3/Smash/Dust/slime_tomb_smash_dust(%d).png' % i )
            BossEffect.Tomb_Smash_img.append(a)
        for i in range(7):
            a = load_image('monster/Goopy/Phase 3/Death/Hit Spark/B/weapon_wide_spark_b_(%d).png' % i )
            BossEffect.Tomb_Die_img.append(a)
        for i in range(16):
            a = load_image('monster/Goopy/Phase 2/Death/Slime/lg_slime_explode(%d).png' % i )
            BossEffect.Slime_explode_img.append(a)
        for i in range(16):
            a = load_image('monster/Goopy/Phase 2/Dust/A/lg_slime_dust_a(%d).png' % i)
            BossEffect.Slime_dust_img.append(a)
            
        if effect.Tomb_Die_dust ==None:
            effect.Tomb_Die_dust= load_image('monster/Goopy/phase 3/Death/dust.png')
        
        effect.Tomb_IntroFrame = 0 
        effect.Tomb_MoveFrame = 0
        effect.Tomb_SmashFrame = 0
        effect.Tomb_DieFrame = 0 
        
    def update(effect,boss):
        if boss.state == 7: ##Intro
            effect.Tomb_IntroFrame = (effect.Tomb_IntroFrame + INTRODUST_ACTION_PER_TIME + INTRODUST_TIME_PER_ACTION * game_framework.frame_time)%36
        elif boss.state == 8: ##Move
            effect.Tomb_MoveFrame = (effect.Tomb_MoveFrame + MOVEDUST_ACTION_PER_TIME + MOVEDUST_TIME_PER_ACTION * game_framework.frame_time)%4
        elif boss.state == 9: ##Die
            effect.Tomb_DieFrame = (effect.Tomb_DieFrame +DIESPARK_ACTION_PER_TIME + DIESPARK_FRAMES_PER_ACTION * game_framework.frame_time)%7
        elif boss.state == 10: ##Smash
            effect.Tomb_SmashFrame = (effect.Tomb_SmashFrame + INTRODUST_ACTION_PER_TIME + INTRODUST_FRAMES_PER_ACTION * game_framework.frame_time )%17
            
    def draw(effect,boss):
        print(boss.state)
        if boss.state == 7: #Tomb_Intro
            effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].clip_composite_draw(0,0,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].w,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].h,0,'n',boss.x,boss.y-200,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].w//1.2,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].h//1.2 )
        
        elif boss.state == 8: #Tomb_Move
            if boss.dir == 1: #오른쪽
                effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].clip_composite_draw(0,0,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].w,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].h,0,'h',boss.x,boss.y-200,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].w//1,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].h//1 )
            else:
                effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].clip_composite_draw(0,0,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].w,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].h,0,'n',boss.x,boss.y-200,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].w//1,effect.Tomb_Move_img[int(effect.Tomb_MoveFrame)].h//1 )
        
        elif boss.state == 9: 
            effect.Tomb_Die_dust.clip_draw(int(effect.Tomb_DieFrame) *460, 5, 450, 420,boss.x,boss.y,450//1.2,420//1.2)
            effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].clip_composite_draw(0,0,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h, 0, 'n' ,  boss.x,boss.y, effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w*2,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h*2)
            ##2번째
            effect.Tomb_Die_dust.clip_draw(int(effect.Tomb_DieFrame) *460, 5, 450, 420,boss.x-100,boss.y+50,450//1.2,420//1.2)
            effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].clip_composite_draw(0,0,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h, 0, 'n' ,  boss.x-100,boss.y+50, effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w*2,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h*2)
            ##3번째
            effect.Tomb_Die_dust.clip_draw(int(effect.Tomb_DieFrame) *460, 5, 450, 420,boss.x+100,boss.y-200,450//1.2,420//1.2)
            effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].clip_composite_draw(0,0,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h, 0, 'n' ,boss.x+100,boss.y-200, effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].w*2,effect.Tomb_Die_img[int(effect.Tomb_DieFrame)].h*2)
            
        elif boss.frame >=10 and boss.state == 10: #Tomb_Smash
            effect.Tomb_Smash_img[int(effect.Tomb_SmashFrame)].clip_composite_draw(0,0,effect.Tomb_Smash_img[int(effect.Tomb_SmashFrame)].w,effect.Tomb_Smash_img[int(effect.Tomb_SmashFrame)].h,0,'n',boss.x,boss.y-210,effect.Tomb_Smash_img[int(effect.Tomb_SmashFrame)].w//1.2,effect.Tomb_Smash_img[int(effect.Tomb_SmashFrame)].h//1.2 )
        
    