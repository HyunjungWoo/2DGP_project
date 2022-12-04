from pico2d import *
import game_framework
import random

##Bullet Frame##
BULLET_FRAMES_PER_ACTION = 4 # 프레임 장수(사진 갯수)
BULLET_TIME_PER_ACTION   = 2.5 #속도 조절
BULLET_ACTION_PER_TIME   = 1.0 / BULLET_TIME_PER_ACTION

### RUN DUST ###
DUST_FRAMES_PER_ACTION = 19# 프레임 장수(사진 갯수)
DUST_TIME_PER_ACTION   = 3#속도 조절
DUST_ACTION_PER_TIME   = 1.0 / DUST_TIME_PER_ACTION

class PlayerEffect:
    ShootEffect = []
    dust_img = None ##달리기 구름 이미지 
    def __init__(effect,player):
        for i in range(4): #총쏘는 이미지 
            a = load_image('resource/aim/shoot_img/shoot_point(%d).png'% i )
            PlayerEffect.ShootEffect.append(a)
        if PlayerEffect.dust_img == None: #달리는 구름 
            PlayerEffect.dust_img = load_image('resource/Run/Normal/run_dust.png')
        effect.BulletFrame = 0 
        effect.dustFrame = 0
        effect.dirR,effect.dirL = 0,0 
        
    def update(effect,player):
        if player.state == 0:##아이들 상태일 때 
            effect.dirR = 0
            effect.dirL = 0  
        elif player.state == 1 or player.state == 6:#달리기 상태 or 달리면서 쏘기 상태 
            effect.dustFrame = (effect.dustFrame + DUST_ACTION_PER_TIME + DUST_TIME_PER_ACTION * game_framework.frame_time)% 19
            if player.direction == -1: ##왼쪽
                effect.dirL += 1
                effect.dirR = 0 
                effect.x = player.x + effect.dirL*1 
            elif player.direction == 1:
                effect.dirR += 1
                effect.dirL = 0 
                effect.x = player.x - effect.dirR*1
            effect.y = player.y    
        elif player.state == 5 or player.state == 6: ##총알 발사 상태 
            effect.BulletFrame = (effect.BulletFrame+ BULLET_ACTION_PER_TIME + BULLET_TIME_PER_ACTION *game_framework.frame_time)%3
            
    def draw(effect,player):
        if player.state == 1 or player.state == 6:
            effect.dust_img.clip_composite_draw(int(effect.dustFrame) *143 , 0,143 ,140,0,'n',effect.x ,effect.y,143//1.2,140//1.2)
            effect.x = player.x
        elif player.state == 5 or player.state == 6: ##총알 발사 상태 
            if player.direction == 1: #오른쪽 
                PlayerEffect.ShootEffect[int(effect.BulletFrame)].clip_composite_draw(0,0,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h,0,'n',player.x+40,player.y,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w//1.2,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h//1.2)
            elif player.direction == -1: #왼쪽
                PlayerEffect.ShootEffect[int(effect.BulletFrame)].clip_composite_draw(0,0,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h,0,'n',player.x-40,player.y,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w//1.2,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h//1.2)
            elif player.direction == 2:
                PlayerEffect.ShootEffect[int(effect.BulletFrame)].clip_composite_draw(0,0,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h,0,'n',player.x+35,player.y+50,PlayerEffect.ShootEffect[int(effect.BulletFrame)].w//1.2,PlayerEffect.ShootEffect[int(effect.BulletFrame)].h//1.2)


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

### EXPLODE ###
EXPLODE_FRAMES_PER_ACTION = 16 # 프레임 장수(사진 갯수)
EXPLODE_TIME_PER_ACTION   = 6#속도 조절
EXPLODE_ACTION_PER_TIME   = 1.0 / EXPLODE_TIME_PER_ACTION


class BossEffect:
    Tomb_Intro_img = []
    Tomb_Move_img = []
    Tomb_Smash_img = []
    Tomb_Die_img = []
    Tomb_Die_dust = None
    Slime_dust_img = []
    Slime_explode_img = []
    Bullet_hit_img = []
    #Bullet_hit_sound = None
    def __init__(effect,boss):
        #인트로 이미지 초기화
        effect.load_image()
        effect.Tomb_IntroFrame = 0 
        effect.Tomb_MoveFrame = 0
        effect.Tomb_SmashFrame = 0
        effect.Tomb_DieFrame = 0 
        effect.SlimeFrame = 0 
        effect.Slime_JumpFram  = 0
        effect.finish = False 
        effect.BulletFrame = 0 
        # if BossEffect.Bullet_hit_sound == None:
        #     BossEffect.Bullet_hit_sound = load_music('resource/Shoot/player_weapon_peashot_death_001.wav')
        #     BossEffect.Bullet_hit_sound.set_volume(30)
    def load_image(effect):
        if BossEffect.Tomb_Intro_img == []:
            for i in range(36):  #3페이즈 인트로 구름 
                a = load_image('monster/Goopy/Phase 3/Dust(Intro)/slime_tomb_dust(%d).png' % i )
                BossEffect.Tomb_Intro_img.append(a)
        if BossEffect.Tomb_Move_img == []:
            for i in range(4): # 3페이즈 움직일 때 구름 
                a = load_image('monster/Goopy/Phase 3/Move/GroundFX/Dust/slime_tomb_groundfx(%d).png' % i )
                BossEffect.Tomb_Move_img.append(a)
        if BossEffect.Tomb_Smash_img ==[]:
            for i in range(17): #3페이즈 스매쉬 구름 
                a = load_image('monster/Goopy/Phase 3/Smash/Dust/slime_tomb_smash_dust(%d).png' % i )
                BossEffect.Tomb_Smash_img.append(a)
        if BossEffect.Tomb_Die_img == []:
            for i in range(7): #3페이즈 죽을 때 번개 
                a = load_image('monster/Goopy/Phase 3/Death/Hit Spark/B/weapon_wide_spark_b_(%d).png' % i )
                BossEffect.Tomb_Die_img.append(a)
        if BossEffect.Slime_dust_img == []:
            for i in range(16): #2페이즈 점프 구름 
                a = load_image('monster/Goopy/Phase 2/Dust/A/lg_slime_dust_a(%d).png' % i)
                BossEffect.Slime_dust_img.append(a)
        if BossEffect.Slime_explode_img ==[]:
            for i in range(16): #페이즈 인트로 슬라임 터지는 이펙트 
                a = load_image('monster/Goopy/Phase 2/Death/Slime/lg_slime_explode(%d).png' % i )
                BossEffect.Slime_explode_img.append(a)    
        if BossEffect.Bullet_hit_img == []:
            for i in range(6): #보스에 부딫힐 때 총알 이미지 
                a = load_image('resource/aim/shoot_img/hit(%d).png'% i )
                BossEffect.Bullet_hit_img.append(a)
        if effect.Tomb_Die_dust ==None: #죽을 때 구름 
            effect.Tomb_Die_dust= load_image('monster/Goopy/phase 3/Death/dust.png')
    def update(effect,boss):
        if boss.state == 1: ##Idle 
            effect.Slime_JumpFram = ( effect.Slime_JumpFram  +  INTRODUST_ACTION_PER_TIME + INTRODUST_FRAMES_PER_ACTION * game_framework.frame_time  )%16
        elif boss.state == 7: ##Intro
            effect.SlimeFrame = (effect.SlimeFrame + EXPLODE_ACTION_PER_TIME + EXPLODE_TIME_PER_ACTION * game_framework.frame_time) % 16
            effect.Tomb_IntroFrame = (effect.Tomb_IntroFrame + INTRODUST_ACTION_PER_TIME + INTRODUST_TIME_PER_ACTION * game_framework.frame_time)%36
            if int(effect.SlimeFrame) == 15: #한번만 터지게 하고싶어서 
                effect.finish = True        
        elif boss.state == 8: ##Move
            effect.Tomb_MoveFrame = (effect.Tomb_MoveFrame + MOVEDUST_ACTION_PER_TIME + MOVEDUST_TIME_PER_ACTION * game_framework.frame_time)%4
        elif boss.state == 9: ##Die
            effect.Tomb_DieFrame = (effect.Tomb_DieFrame +DIESPARK_ACTION_PER_TIME + DIESPARK_FRAMES_PER_ACTION * game_framework.frame_time)%7
        elif boss.state == 10: ##Smash
            effect.Tomb_SmashFrame = (effect.Tomb_SmashFrame + INTRODUST_ACTION_PER_TIME + INTRODUST_FRAMES_PER_ACTION * game_framework.frame_time )%17
        
        if boss.bosshit == True:
            effect.BulletFrame = (effect.BulletFrame + INTRODUST_ACTION_PER_TIME + INTRODUST_TIME_PER_ACTION * game_framework.frame_time) % 6
           # BossEffect.Bullet_hit_sound.play(1)

    def draw(effect,boss):
        if boss.bosshit == True:
            effect.Bullet_hit_img[int(effect.BulletFrame)].clip_composite_draw(0,0,effect.Bullet_hit_img[int(effect.BulletFrame)].w,effect.Bullet_hit_img[int(effect.BulletFrame)].h,0,'n',random.randint(boss.x-50,boss.x+50),random.randint(boss.y-50,boss.y+50),effect.Bullet_hit_img[int(effect.BulletFrame)].w,effect.Bullet_hit_img[int(effect.BulletFrame)].h//1.2)
        if boss.state == 1: #Idle
            if boss.change_morph == False: 
                effect.Slime_dust_img[int(effect.Slime_JumpFram)].clip_composite_draw(0,0,effect.Slime_dust_img[int(effect.Slime_JumpFram)].w,effect.Slime_dust_img[int(effect.Slime_JumpFram)].h,0,'n',boss.x,boss.y,effect.Slime_dust_img[int(effect.Slime_JumpFram)].w//1.2,effect.Slime_dust_img[int(effect.Slime_JumpFram)].h//1.2)
            else : 
                effect.Slime_dust_img[int(effect.Slime_JumpFram)].clip_composite_draw(0,0,effect.Slime_dust_img[int(effect.Slime_JumpFram)].w,effect.Slime_dust_img[int(effect.Slime_JumpFram)].h,0,'n',boss.x,boss.y-50,effect.Slime_dust_img[int(effect.Slime_JumpFram)].w,effect.Slime_dust_img[int(effect.Slime_JumpFram)].h)
        elif boss.state == 7: #Tomb_Intro
            effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].clip_composite_draw(0,0,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].w,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].h,0,'n',boss.x,boss.y-200,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].w//1.2,effect.Tomb_Intro_img[int(effect.Tomb_IntroFrame)].h//1.2 )
            if effect.finish == False:
                effect.Slime_explode_img[int(effect.SlimeFrame)].clip_composite_draw(0,0,effect.Slime_explode_img[int(effect.SlimeFrame)].w,effect.Slime_explode_img[int(effect.SlimeFrame)].h,0,'n',boss.x,boss.y-100,effect.Slime_explode_img[int(effect.SlimeFrame)].w//1.2,effect.Slime_explode_img[int(effect.SlimeFrame)].h//1.2)

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



