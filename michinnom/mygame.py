import game_framework
import pico2d
import logo_state
import play_state
import ready_state
import die_state
import clear_state
#pico2d.open_canvas(1280,720,sync=True,full=True) #풀스크린 적용 
pico2d.open_canvas(1280,720,sync=True) 
game_framework.run(logo_state)
pico2d.close_canvas() 


