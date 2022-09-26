from pico2d import *
open_canvas()
grass = load_image('grass.png')
character_walk = load_image('walkingcarby.png')
character_run = load_image('runningcarby.png')
character_jump = load_image('jumppingcarby.png')
character_spin = load_image('spincarby.png')
character_attack = load_image('attackcarby.png')

def carby_walking():
    x = 0
    frame = 0
    while (x<800):
        clear_canvas()
        grass.draw(400, 30)
        character_walk.clip_draw(frame * 70, 0, 25, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 7
        x += 5
        delay(0.05)
        get_events()

def carby_running():
    x = 0
    frame = 0
    while (x<800):
        clear_canvas()
        grass.draw(400, 30)
        character_run.clip_draw(frame * 70, 0, 20, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 5
        x += 5
        delay(0.05)
        get_events()

def carby_jumpping():
    x, y = 0, 70
    frame = 0
    while (x<800):
        if y%2==0:
            clear_canvas()
            grass.draw(400, 30)
            character_jump.clip_draw(frame * 70, 0, 20, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 7
            x += 5
            y += 35
            delay(0.05)
            get_events()
        else:
            clear_canvas()
            grass.draw(400, 30)
            character_jump.clip_draw(frame * 70, 0, 20, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 7
            x += 5
            y -= 35
            delay(0.05)
            get_events()

def carby_spinning():
    x, y = 0, 30
    frame = 0
    while (x<800):
        clear_canvas()
        grass.draw(400, 30)
        character_spin.clip_draw(frame * 70, 0, 43, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        y += 5
        if y>600:
            y -= 50
        delay(0.05)
        get_events()

def carby_attack():
    x = 100
    frame = 0
    while (x<150):
        clear_canvas()
        grass.draw(400, 30)
        character_attack.clip_draw(frame * 50, 0, 20, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 9
        x += 5
        delay(0.05)
        get_events()


carby_walking()
carby_running()
carby_jumpping()
carby_spinning()
carby_attack()
close_canvas()
