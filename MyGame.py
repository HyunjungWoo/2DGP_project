import game_framework
import pico2d
import logo_state
import play_state

pico2d.open_canvas(1280,720)
game_framework.run(logo_state)
pico2d.close_canvas()