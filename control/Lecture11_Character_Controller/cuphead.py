from pico2d import *
import game_framework

class CupHead:
    pass

key_event_table = {
    (SDL_KEYDOWN,SDLK_RIGHT):RD,
    (SDL_KEYDOWN,SDLK_LEFT):LD,
    (SDL_KEYUP,SDLK_RIGHT):RU,
    (SDL_KEYUP,SDLK_LEFT):LU,
    (SDL_KEYDOWN,SDLK_c):CD,
    (SDL_KEYUP,SDLK_c):CU
}