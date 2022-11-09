import sys
import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Boy() for i in range(1000)]


grass = Grass()

running = True;
while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()
