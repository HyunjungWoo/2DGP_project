import pico2d
import play_state

pico2d.open_canvas()
play_state.enter()

while play_state.running:
    play_state.handle_events()
    play_state.update()
    play_state.draw()

play_state.exit()

pico2d.close_canvas()
