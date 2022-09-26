import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r + math.cos(deg / 360 *2 * math.pi)
        y = cy + r + math.sin(deg / 360 *2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(1)

def run_rectangle():
    for x in range(750, 50, -10):
        character.draw_now(x,y)
    for y in range(600, 50, -10):
         character.draw_now(x,y)
    pass

while True:
    run_circle()
    run_rectangle()
    break


close_canvas()
